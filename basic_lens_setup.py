from UFOpticSim import *

sim = Simulation(media='air', interval_cm=1)

pulse = PulseProfile(duration_fs=30, bandwidth_nm=45, is_temporally_limited=True, central_wavelength_nm=800, beam_waist_mm=0.5, m2=1)
laser = Laser(beam_profile=pulse, dir=(1, 0), pos_cm2=(1, 1))
glass = Material(media='BK7', thickness_mm=10)
lens = Lens(material=glass, focal_length_mm=100, pos_cm2=(2, 1))
screen = Screen(pos_cm2=(3, 1))

sim.add_laser(laser)
sim.add_element(lens)
sim.add_screen(screen)

sim.print()
results = sim.run()
results.print()