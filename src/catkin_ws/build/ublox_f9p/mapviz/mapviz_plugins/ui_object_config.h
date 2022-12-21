/********************************************************************************
** Form generated from reading UI file 'object_config.ui'
**
** Created by: Qt User Interface Compiler version 5.9.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_OBJECT_CONFIG_H
#define UI_OBJECT_CONFIG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>
#include <mapviz/color_button.h>

QT_BEGIN_NAMESPACE

class Ui_object_config
{
public:
    QGridLayout *gridLayout;
    QLabel *status;
    QLineEdit *topic;
    QLabel *label_2;
    QPushButton *selecttopic;
    QLabel *label;
    QLabel *label_3;
    mapviz::ColorButton *color;
    QLabel *label_4;
    QCheckBox *show_ids;

    void setupUi(QWidget *object_config)
    {
        if (object_config->objectName().isEmpty())
            object_config->setObjectName(QStringLiteral("object_config"));
        object_config->resize(400, 300);
        object_config->setStyleSheet(QStringLiteral(""));
        gridLayout = new QGridLayout(object_config);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setVerticalSpacing(4);
        gridLayout->setContentsMargins(2, 2, 2, 2);
        status = new QLabel(object_config);
        status->setObjectName(QStringLiteral("status"));
        QFont font;
        font.setFamily(QStringLiteral("Sans Serif"));
        font.setPointSize(8);
        status->setFont(font);
        status->setStyleSheet(QStringLiteral(""));
        status->setWordWrap(true);

        gridLayout->addWidget(status, 5, 3, 1, 2);

        topic = new QLineEdit(object_config);
        topic->setObjectName(QStringLiteral("topic"));
        topic->setFont(font);

        gridLayout->addWidget(topic, 2, 3, 1, 1);

        label_2 = new QLabel(object_config);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setFont(font);

        gridLayout->addWidget(label_2, 5, 0, 1, 1);

        selecttopic = new QPushButton(object_config);
        selecttopic->setObjectName(QStringLiteral("selecttopic"));
        selecttopic->setMaximumSize(QSize(55, 16777215));
        selecttopic->setFont(font);
        selecttopic->setStyleSheet(QStringLiteral(""));

        gridLayout->addWidget(selecttopic, 2, 4, 1, 1);

        label = new QLabel(object_config);
        label->setObjectName(QStringLiteral("label"));
        label->setFont(font);

        gridLayout->addWidget(label, 2, 0, 1, 1);

        label_3 = new QLabel(object_config);
        label_3->setObjectName(QStringLiteral("label_3"));

        gridLayout->addWidget(label_3, 3, 0, 1, 1);

        color = new mapviz::ColorButton(object_config);
        color->setObjectName(QStringLiteral("color"));
        color->setMaximumSize(QSize(24, 24));
        color->setAutoFillBackground(false);
        color->setStyleSheet(QStringLiteral(""));

        gridLayout->addWidget(color, 3, 3, 1, 1);

        label_4 = new QLabel(object_config);
        label_4->setObjectName(QStringLiteral("label_4"));

        gridLayout->addWidget(label_4, 4, 0, 1, 1);

        show_ids = new QCheckBox(object_config);
        show_ids->setObjectName(QStringLiteral("show_ids"));

        gridLayout->addWidget(show_ids, 4, 3, 1, 1);


        retranslateUi(object_config);

        QMetaObject::connectSlotsByName(object_config);
    } // setupUi

    void retranslateUi(QWidget *object_config)
    {
        object_config->setWindowTitle(QApplication::translate("object_config", "Form", Q_NULLPTR));
        status->setText(QApplication::translate("object_config", "No topic", Q_NULLPTR));
        label_2->setText(QApplication::translate("object_config", "Status:", Q_NULLPTR));
        selecttopic->setText(QApplication::translate("object_config", "Select", Q_NULLPTR));
        label->setText(QApplication::translate("object_config", "Topic:", Q_NULLPTR));
        label_3->setText(QApplication::translate("object_config", "Color:", Q_NULLPTR));
        color->setText(QString());
        label_4->setText(QApplication::translate("object_config", "Show IDs:", Q_NULLPTR));
        show_ids->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class object_config: public Ui_object_config {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_OBJECT_CONFIG_H
