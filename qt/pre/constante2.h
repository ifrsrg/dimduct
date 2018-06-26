#ifndef CONSTANTE2_H
#define CONSTANTE2_H

#include <QWidget>

namespace Ui {
class Constante2;
}

class Constante2 : public QWidget
{
    Q_OBJECT

public:
    explicit Constante2(QWidget *parent = 0);
    ~Constante2();

private:
    Ui::Constante2 *ui;
};

#endif // CONSTANTE2_H
