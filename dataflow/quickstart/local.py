import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText


def run():
  with beam.Pipeline() as p:

    # Read the local file into a PCollection
    lines = p | ReadFromText('corpus.txt')

    # And write the text to a new local file
    output = lines | WriteToText('output')


if __name__ == '__main__':
  run()
