#ifndef ARBITRARIA_H
#define ARBITRARIA_H

#include <QWidget>

namespace Ui {
class arbitraria;
}

class Arbitraria : public QWidget
{
    Q_OBJECT

public:
    explicit Arbitraria(QWidget *parent = 0);
    ~Arbitraria();

private:
    Ui::arbitraria *ui;
};

#endif // ARBITRARIA_H
