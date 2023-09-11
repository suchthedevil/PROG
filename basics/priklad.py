a = 1
b = 0.3
c = 0.5
sklo = 0.01
ro_sklo = 2500
ro_voda = 998

v_voda = (a-sklo*2)*(b-sklo*2)*(c-sklo)
v_total = a*b*c
v_sklo = v_total - v_voda

m_voda = ro_voda*v_voda
m_sklo = ro_sklo*v_sklo
m_total = m_voda + m_sklo

print(m_total)

