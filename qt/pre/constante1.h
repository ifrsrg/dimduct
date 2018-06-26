#ifndef CONSTANTE1_H
#define CONSTANTE1_H

#include <QWidget>

namespace Ui {
class Constante1;
}

class Constante1 : public QWidget
{
    Q_OBJECT

public:
    explicit Constante1(QWidget *parent = 0);
    ~Constante1();

private:
    Ui::Constante1 *ui;
};

#endif // CONSTANTE1_H
