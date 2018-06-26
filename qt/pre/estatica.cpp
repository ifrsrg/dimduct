#include "estatica.h"
#include "ui_estatica.h"

Estatica::Estatica(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Estatica)
{
    ui->setupUi(this);
}

Estatica::~Estatica()
{
    delete ui;
}
