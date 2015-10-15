Business = [ 'Update', 'Infrastructure', 'Foreign Trade', 'E-Commerce', 'Policy and Corporate', 'Special', 'Commodity']

with open('regional1.txt') as fr, open('sports.txt') as fs, \
open('bollywood.txt') as fb, open('gallery.txt') as fg, \
open('gadgets.txt') as fga, open('money.txt') as fm, \
open('jokes.txt') as fj, open('lifestyle.txt') as fl, \
open('magazines.txt') as fmag, open('abhivyakti.txt') as fabhi, \
open('international.txt') as finter, open('national.txt') as fnat, \
open('states.txt') as fstates, open('jeevan_mantra.txt') as fjeev, \
open('regional2.txt') as fr2:
	data_region = fr.read().splitlines()
	data_sports = fs.read().splitlines()
	data_bolly = fb.read().splitlines()
	data_gal = fg.read().splitlines()
	data_gadget = fga.read().splitlines()
	data_money = fm.read().splitlines()
	data_jokes = fj.read().splitlines()
	data_life = fl.read().splitlines()
	data_mag = fmag.read().splitlines()
	data_abhi = fabhi.read().splitlines()
	data_inter = finter.read().splitlines()
	data_national = fnat.read().splitlines()
	data_states = fstates.read().splitlines()
	data_jeev = fjeev.read().splitlines()
	data_region2 = fr2.read().splitlines()
	


# data = data_region + data_sports + data_bolly + data_gal + data_gadget + \
# data_money + data_jokes + data_life + data_mag + data_abhi + data_inter + \
# data_national + data_states + data_jeev + data_region2

# len(set(mydict.keys())-set(data))
# set(mydict.keys())-set(data)
