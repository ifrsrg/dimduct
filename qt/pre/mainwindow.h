#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_button_arbitrario_clicked();

    void on_button_constante1_clicked();

    void on_button_constante2_clicked();

    void on_button_estatica_clicked();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
