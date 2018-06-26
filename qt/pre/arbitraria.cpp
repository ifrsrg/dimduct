#include "arbitraria.h"
#include "ui_arbitraria.h"

Arbitraria::Arbitraria(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::arbitraria)
{
    ui->setupUi(this);
}

Arbitraria::~Arbitraria()
{
    delete ui;
}
