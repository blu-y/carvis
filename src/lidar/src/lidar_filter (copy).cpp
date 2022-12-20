#include <ros/ros.h>
#include <sensor_msgs/PointCloud2.h>

#include <pcl_conversions/pcl_conversions.h>

// PCL specific includes
#include <pcl/conversions.h>
#include <pcl/filters/voxel_grid.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl/filters/passthrough.h>

ros::Publisher pub;

// This is to save on typing
typedef pcl::PointCloud<pcl::PointXYZ> point_cloud_t;

void cloud_cb (const sensor_msgs::PointCloud2& ros_pc)
{
    // See http://wiki.ros.org/hydro/Migration for the source of this magic.
    pcl::PCLPointCloud2 pcl_pc; // temporary PointCloud2 intermediary
    pcl_conversions::toPCL(ros_pc, pcl_pc);

    // Convert point cloud to PCL native point cloud
    point_cloud_t::Ptr input_ptr(new point_cloud_t());
    point_cloud_t::Ptr cloud_filtered(new point_cloud_t());
    //pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_filtered (new pcl::PointCloud<pcl::PointXYZ>);

    pcl::fromPCLPointCloud2(pcl_pc, *input_ptr);

    // Set up VoxelGrid filter to bin into 10cm grid
    pcl::VoxelGrid<pcl::PointXYZ> sor;
    sor.setInputCloud(input_ptr);
    sor.setLeafSize(0.2, 0.2, 0.2);

    // Create output point cloud
    point_cloud_t::Ptr output_ptr(new point_cloud_t());

    // Run filter
    sor.filter(*output_ptr);

    pcl::PassThrough<pcl::PointXYZ> passz;
    passz.setInputCloud (output_ptr);                //입력 
    passz.setFilterFieldName ("z");             //적용할 좌표 축 (eg. Z축)
    passz.setFilterLimits (-0.60, 999);          //적용할 값 (최소, 최대 값)
    passz.filter (*cloud_filtered);             //필터 적용

    pcl::PassThrough<pcl::PointXYZ> passy;
    passy.setInputCloud (cloud_filtered);                //입력 
    passy.setFilterFieldName ("y");             //적용할 좌표 축 (eg. Z축)
    passy.setFilterLimits (-20, 20);          //적용할 값 (최소, 최대 값)
    passy.filter (*cloud_filtered);             //필터 적용

    pcl::PassThrough<pcl::PointXYZ> passx;
    passx.setInputCloud (cloud_filtered);                //입력 
    passx.setFilterFieldName ("x");             //적용할 좌표 축 (eg. Z축)
    passx.setFilterLimits (-20, 20);          //적용할 값 (최소, 최대 값)
    passx.filter (*cloud_filtered);             //필터 적용

    // pass.setFilterLimitsNegative(true)

    // Now covert output back from PCL native type to ROS
    sensor_msgs::PointCloud2 ros_output;
    pcl::toPCLPointCloud2(*cloud_filtered, pcl_pc);
    pcl_conversions::fromPCL(pcl_pc, ros_output);

    // Publish the data
    pub.publish(ros_output);
}

int main (int argc, char** argv)
{
    // Initialize ROS
    ros::init (argc, argv, "pcl_filter");
    ros::NodeHandle nh;

    // Create a ROS subscriber for the input point cloud
    ros::Subscriber sub = nh.subscribe("/velodyne_points", 1, cloud_cb);

    // Create a ROS publisher for the output point cloud
    pub = nh.advertise<sensor_msgs::PointCloud2>("/velodyne_points_filtered", 1);

    // Spin
    ros::spin ();
}
