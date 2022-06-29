import numpy as np
import skfuzzy as fuzz


def calcula_propina(calidad,servicio):
	x_qual = np.arange(0,11,1)
	x_serv= np.arange(0,11,1)
	x_tip = np.arange(0,26,1)


	qual_lo = fuzz.trimf(x_qual, [0,0,5])
	qual_md = fuzz.trimf(x_qual, [0,5,10])
	qual_hi = fuzz.trimf(x_qual,[0,10,10])
	serv_lo = fuzz.trimf(x_serv, [0,0,5])
	serv_md = fuzz.trimf(x_serv, [0,5,10])
	serv_hi = fuzz.trimf(x_serv,[0,10,10])
	tip_lo = fuzz.trimf(x_tip,[0,0,13])
	tip_md = fuzz.trimf(x_tip,[0,13,25])
	tip_hi = fuzz.trimf(x_tip,[13,25,25])


	qual_level_lo = fuzz.interp_membership(x_qual,qual_lo, calidad)
	qual_level_md = fuzz.interp_membership(x_qual,qual_md, calidad)
	qual_level_hi = fuzz.interp_membership(x_qual,qual_hi, calidad)

	serv_level_lo = fuzz.interp_membership(x_serv, serv_lo, servicio)
	serv_level_md = fuzz.interp_membership(x_serv, serv_md, servicio)
	serv_level_hi = fuzz.interp_membership(x_serv, serv_hi, servicio)

	#For rule 1
	active_rule1 = np.fmin(qual_level_lo, serv_level_lo)
	tip_activation_lo = np.fmin(active_rule1, tip_lo)

	#Rule 2
	tip_activation_md = np.fmin(serv_level_md,tip_md)

	#Rule 3
	active_rule3 = np.fmax(qual_level_hi,serv_level_hi)
	tip_activation_hi = np.fmin(active_rule3, tip_hi)

	#Aggregate the output 
	aggregated = np.fmax(tip_activation_lo, np.fmax(tip_activation_md,
	                                                tip_activation_hi))

	# Defuzzifuy the aggregated area to get the crisp output

	tip = fuzz.defuzz(x_tip, aggregated,'centroid')
	return tip