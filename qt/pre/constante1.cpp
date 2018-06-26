#include "constante1.h"
#include "ui_constante1.h"

Constante1::Constante1(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Constante1)
{
    ui->setupUi(this);
}

Constante1::~Constante1()
{
    delete ui;
}
