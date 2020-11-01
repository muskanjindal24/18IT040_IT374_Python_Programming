#multipleInheritance
class Cloud:
    Job = 'Cloud'
    company = 'Amazon'

class JobProfile:
    Certifications = True
    Job = 'Cloud Architect'

class Details(JobProfile, Cloud):
    def __init__(self):
        print('Job: {}'.format(self.Job))
        print('Company Name: {}'.format(self.company))
        if self.Certifications is True:
            print('Amazon Certified')

#multilevelInheritance
class MusicalInstrument:
    num_of_major_keys = 12
 
class StringInstrument(MusicalInstrument):
    type_of_wood = 'Tonewood'
  
class Guitar(StringInstrument):
    def __init__(self):
        self.num_of_strings = 6
        print('The guitar consists of {} strings, it is made of {} and can play {} keys.'
              .format(self.num_of_strings,
                      self.type_of_wood, self.num_of_major_keys))

Details = Details()
guitar = Guitar()