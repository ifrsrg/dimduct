#ifndef ESTATICA_H
#define ESTATICA_H

#include <QWidget>

namespace Ui {
class Estatica;
}

class Estatica : public QWidget
{
    Q_OBJECT

public:
    explicit Estatica(QWidget *parent = 0);
    ~Estatica();

private:
    Ui::Estatica *ui;
};

#endif // ESTATICA_H
