#include <ros/ros.h>
#include <sensor_msgs/PointCloud2.h>

#include <pcl_conversions/pcl_conversions.h>

// PCL specific includes
#include <pcl/conversions.h>
#include <pcl/filters/voxel_grid.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl/filters/passthrough.h>
#include <pcl/kdtree/kdtree.h>
#include <pcl/filters/extract_indices.h>
#include <pcl/sample_consensus/method_types.h>
#include <pcl/sample_consensus/model_types.h>
//#include <pcl/segmentation/sac_segmentation.h>
#include <pcl/segmentation/extract_clusters.h>

ros::Publisher pub_f;
ros::Publisher pub_c;

// This is to save on typing
typedef pcl::PointCloud<pcl::PointXYZI> point_cloud_t;

void cloud_cb (const sensor_msgs::PointCloud2& ros_pc)
{
    // See http://wiki.ros.org/hydro/Migration for the source of this magic.
    pcl::PCLPointCloud2 pcl_pc; // temporary PointCloud2 intermediary
    pcl_conversions::toPCL(ros_pc, pcl_pc);

    // Convert point cloud to PCL native point cloud
    point_cloud_t::Ptr input_ptr(new point_cloud_t());
    point_cloud_t::Ptr cloud_filtered(new point_cloud_t());
    //pcl::PointCloud<pcl::PointXYZI>::Ptr cloud_filtered (new pcl::PointCloud<pcl::PointXYZI>);

    pcl::fromPCLPointCloud2(pcl_pc, *input_ptr);

    // Set up VoxelGrid filter to bin into 10cm grid
    pcl::VoxelGrid<pcl::PointXYZI> sor;
    sor.setInputCloud(input_ptr);
    sor.setLeafSize(0.1, 0.1, 0.1);
    // Create output point cloud
    point_cloud_t::Ptr output_ptr(new point_cloud_t());
    // Run filter
    sor.filter(*output_ptr);

    // ROI
    pcl::PassThrough<pcl::PointXYZI> passz;
    passz.setInputCloud (output_ptr);                //입력 
    passz.setFilterFieldName ("z");             //적용할 좌표 축 (eg. Z축)
    passz.setFilterLimits (-0.3, 999);          //적용할 값 (최소, 최대 값)
    passz.filter (*cloud_filtered);             //필터 적용
    pcl::PassThrough<pcl::PointXYZI> passy;
    passy.setInputCloud (cloud_filtered);                //입력 
    passy.setFilterFieldName ("y");             //적용할 좌표 축 (eg. Z축)
    passy.setFilterLimits (-10, 10);          //적용할 값 (최소, 최대 값)
    passy.filter (*cloud_filtered);             //필터 적용
    pcl::PassThrough<pcl::PointXYZI> passx;
    passx.setInputCloud (cloud_filtered);                //입력 
    passx.setFilterFieldName ("x");             //적용할 좌표 축 (eg. Z축)
    passx.setFilterLimits (-3, 30);          //적용할 값 (최소, 최대 값)
    passx.filter (*cloud_filtered);             //필터 적용
    // pass.setFilterLimitsNegative(true)
    // Now covert output back from PCL native type to ROS
    // Publish the data
    sensor_msgs::PointCloud2 ros_output;
    pcl::toPCLPointCloud2(*cloud_filtered, pcl_pc);
    pcl_conversions::fromPCL(pcl_pc, ros_output);
    pub_f.publish(ros_output);

    // Cluster
    pcl::search::KdTree<pcl::PointXYZI>::Ptr tree(new pcl::search::KdTree<pcl::PointXYZI>);
    tree->setInputCloud (cloud_filtered);
    std::vector<pcl::PointIndices> cluster_indices;
    pcl::EuclideanClusterExtraction<pcl::PointXYZI> ec;
    ec.setInputCloud (cloud_filtered);
    ec.setClusterTolerance (0.6);
    ec.setMinClusterSize (5);
    ec.setMaxClusterSize (2000);
    ec.setSearchMethod (tree);
    ec.extract (cluster_indices);
    //std::cout << "Number of cluster: " << cluster_indices.size () << std::endl;

    // Cluster_visualize with I
    pcl::PointCloud<pcl::PointXYZI> TotalCloud;
    int j = 0;
    for (std::vector<pcl::PointIndices>::const_iterator it = cluster_indices.begin (); it != cluster_indices.end (); ++it)
    {
        //pcl::PointCloud<pcl::PointXYZI>::Ptr cloud_cluster (new pcl::PointCloud<pcl::PointXYZI>);
        for (std::vector<int>::const_iterator pit = it->indices.begin (); pit != it->indices.end (); ++pit)
        {
            pcl::PointXYZI pt = cloud_filtered->points[*pit];
            pcl::PointXYZI pt2;
            
            pt2.x = pt.x, pt2.y = pt.y, pt2.z = pt.z;
            pt2.intensity = (float)(j + 1);

            TotalCloud.push_back(pt2);
            //cloud_cluster->points.push_back (cloud_filtered->points[*pit]);
        }
        //cloud_cluster->width = cloud_cluster->points.size ();
        //cloud_cluster->height = 1;
        //cloud_cluster->is_dense = true;
        //std::cout << "PointCloud representing the Cluster: " << j << cloud_cluster->points.size () << " data points." << std::endl;
        j++;
    }
    
    // Publish Clustered data with ROS
    pcl::PCLPointCloud2 cloud_clustered;
    sensor_msgs::PointCloud2 ros_output_clustered;
    pcl::toPCLPointCloud2(TotalCloud, cloud_clustered);
    pcl_conversions::fromPCL(cloud_clustered, ros_output_clustered);
    ros_output_clustered.header.frame_id = "velodyne";
    // Publish the data
    pub_c.publish(ros_output_clustered);
}

int main (int argc, char** argv)
{
    // Initialize ROS
    ros::init (argc, argv, "pcl_filter");
    ros::NodeHandle nh;

    // Create a ROS subscriber for the input point cloud
    ros::Subscriber sub = nh.subscribe("/velodyne_points", 1, cloud_cb);

    // Create a ROS publisher for the output point cloud
    pub_f = nh.advertise<sensor_msgs::PointCloud2>("/velodyne_points_filtered", 1);
    pub_c = nh.advertise<sensor_msgs::PointCloud2>("/velodyne_points_clustered", 1);
    // Spin
    ros::spin ();
}
