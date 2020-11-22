from CoolProp.HumidAirProp import HAPropsSI
from CoolProp.CoolProp import PropsSI

#Hyper parameter
#P_Pa_Pressure
#T_K_Temperature;
#D_kg/m^3_Mass density;
#Q_mol/mol_Mass vapor quality
#H_J/kg_Enthalpy

p = 101325
t = PropsSI('T', 'P', p, 'Q', 0, 'Water')
print('\n-------------CoolProp-------------')
print('- 在 {} Pa(abs) 时，水的饱和温度: {:.2f} K \n'.format(p, t))    # 373.12 K

class WaterProp(object):
    # 求特定压力下的物性
    def __init__(self, p=101325):
        self.T = PropsSI('T', 'P', p, 'Q', 0, 'Water')          # 饱和温度
        self.C = PropsSI('C', 'P', p, 'Q', 0, 'Water')          # 比热容
        self.D_l = PropsSI('D', 'P', p, 'Q', 0, 'Water')        # 液体密度
        self.D_v = PropsSI('D', 'P', p, 'Q', 1, 'Water')        # 蒸汽密度

        self.H_l = PropsSI('H', 'P', p, 'Q', 0, 'Water')
        self.H_v = PropsSI('H', 'P', p, 'Q', 1, 'Water')
        self.H = self.H_v - self.H_l                            # 汽化潜热
        self.L_l = PropsSI('L', 'P', p, 'Q', 0, 'Water')        # 导热系数
        self.I_l = PropsSI('I', 'P', p, 'Q', 0, 'Water')        # 表面张力

        self.U_l = PropsSI('V', 'P', p, 'Q', 0, 'Water')        # 动力粘度
        self.V_l = self.U_l / self.D_l                          # 运动粘度
        self.Prl = PropsSI('Prandtl', 'P', p, 'Q', 0, 'Water')  # 普朗特数

        self.print_prop()

    def print_prop(self):
        print('\n-------------CoolProp-------------')
        print('- {}: {:>10s}      {:<10}'.format('介质名称', 'Water',    '单位'))
        print('- {}: {:>10.2f}    {:<10}'.format('计算压力', p,          'Pa'))
        print('- {}: {:>10.2f}    {:<10}'.format('饱和温度', self.T,     'K'))
        print('- {}: {:>10.2f}    {:<10}'.format('液体密度ρ液', self.D_l,   'kg/m3'))
        print('- {}: {:>10.4f}    {:<10}'.format('蒸汽密度ρ气', self.D_v,   'kg/m3'))
        print('- {}: {:>10.2f}    {:<10}'.format('汽化潜热', self.H,     'J/kg'))
        print('- {}: {:>10.4f}    {:<10}'.format('导热系数λ', self.L_l,   'W/m.K'))
        print('- {}: {:>10.4e}    {:<10}'.format('运动粘度η', self.V_l,   'm2/s'))
        print('- {}: {:>10.4f}    {:<10}'.format('普朗特数pr', self.Prl,   '-'))


WaterProp(p=101325)
'''
- 介质名称:      Water      单位
- 计算压力:  101325.00    Pa
- 饱和温度:     373.12    K
- 液体密度:     958.37    kg/m3
- 蒸汽密度:     0.5977    kg/m3
- 汽化潜热: 2256471.59    J/kg
- 导热系数:     0.6772    W/m.K
- 运动粘度: 2.9389e-07    m2/s
- 普朗特数:     1.7533    
'''






