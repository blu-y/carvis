/****************************************************************************
** Meta object code from reading C++ file 'tf_frame_plugin.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.9.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../../../src/mapviz/mapviz_plugins/include/mapviz_plugins/tf_frame_plugin.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'tf_frame_plugin.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.9.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_mapviz_plugins__TfFramePlugin_t {
    QByteArrayData data[4];
    char stringdata0[55];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_mapviz_plugins__TfFramePlugin_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_mapviz_plugins__TfFramePlugin_t qt_meta_stringdata_mapviz_plugins__TfFramePlugin = {
    {
QT_MOC_LITERAL(0, 0, 29), // "mapviz_plugins::TfFramePlugin"
QT_MOC_LITERAL(1, 30, 11), // "SelectFrame"
QT_MOC_LITERAL(2, 42, 0), // ""
QT_MOC_LITERAL(3, 43, 11) // "FrameEdited"

    },
    "mapviz_plugins::TfFramePlugin\0SelectFrame\0"
    "\0FrameEdited"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_mapviz_plugins__TfFramePlugin[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    0,   24,    2, 0x09 /* Protected */,
       3,    0,   25,    2, 0x09 /* Protected */,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void mapviz_plugins::TfFramePlugin::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        TfFramePlugin *_t = static_cast<TfFramePlugin *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->SelectFrame(); break;
        case 1: _t->FrameEdited(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObject mapviz_plugins::TfFramePlugin::staticMetaObject = {
    { &mapviz_plugins::PointDrawingPlugin::staticMetaObject, qt_meta_stringdata_mapviz_plugins__TfFramePlugin.data,
      qt_meta_data_mapviz_plugins__TfFramePlugin,  qt_static_metacall, nullptr, nullptr}
};


const QMetaObject *mapviz_plugins::TfFramePlugin::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *mapviz_plugins::TfFramePlugin::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_mapviz_plugins__TfFramePlugin.stringdata0))
        return static_cast<void*>(this);
    return mapviz_plugins::PointDrawingPlugin::qt_metacast(_clname);
}

int mapviz_plugins::TfFramePlugin::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = mapviz_plugins::PointDrawingPlugin::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 2;
    }
    return _id;
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE