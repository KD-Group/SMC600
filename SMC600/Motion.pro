QT       += core gui
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = SMC600
TEMPLATE = app

SOURCES += main.cpp

HEADERS  += smc600.h \
    LTSMC.h

win32: LIBS += -L$$PWD/ -lLTDMC
INCLUDEPATH += $$PWD/
DEPENDPATH += $$PWD/
