def parseData(data, self):
    self.religion = data.get('religion')
    self.denomination = data.get('denomination')
    self.color = 'teal'
    self.filled = True

    return self
