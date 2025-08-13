from UFOpticSim import Simulation, Screen, PulseProfile, Laser, Lens, Mirror, Material

sim = Simulation(media='air', interval_cm=0.5)

pulse = PulseProfile(duration_fs=30, bandwidth_nm=45, is_temporally_limited=True, central_wavelength_nm=800, beam_waist_mm=0.5, m2=1)
laser = Laser(beam_profile=pulse, dir=(1, 0), pos_cm2=(1, 1))
glass = Material(media='BK7', thickness_mm=10)
lens = Lens(material=glass, focal_length_mm=100, pos_cm2=(2, 1), lens_name="Lens 1")
mirror = Mirror(material=glass, angle_to_horizontal=45, pos_cm2=(3, 1), mirror_name="Mirror 1")
screen = Screen(pos_cm2=(3, 2))

sim.add_laser(laser)
sim.add_element(mirror)
sim.add_element(lens)
sim.add_screen(screen)

sim.run(output=True, visualisation=True)