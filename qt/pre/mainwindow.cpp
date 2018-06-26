#include "mainwindow.h"
#include "arbitraria.h"
#include "constante1.h"
#include "constante2.h"
#include "estatica.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_button_arbitrario_clicked()
{
    Arbitraria *arb = new Arbitraria;
    arb->show();
}

void MainWindow::on_button_constante1_clicked()
{
    Constante1 *arb = new Constante1;
    arb->show();
}

void MainWindow::on_button_constante2_clicked()
{
    Constante2 *arb = new Constante2;
    arb->show();
}

void MainWindow::on_button_estatica_clicked()
{
    Estatica *arb = new Estatica;
    arb->show();
}
