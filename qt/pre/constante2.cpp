#include "constante2.h"
#include "ui_constante2.h"

Constante2::Constante2(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Constante2)
{
    ui->setupUi(this);
}

Constante2::~Constante2()
{
    delete ui;
}
