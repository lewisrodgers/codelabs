import argparse

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions


def run(argv=None):
  parser = argparse.ArgumentParser()
  parser.add_argument('--input',
                      dest='input',
                      default='gs://',
                      help='Input file to process.')
  parser.add_argument('--output',
                      dest='output',
                      # CHANGE 1/5: The Google Cloud Storage path is required
                      # for outputting the results.
                      default='gs://YOUR_OUTPUT_BUCKET/AND_OUTPUT_PREFIX',
                      help='Output file to write results to.')
  known_args, pipeline_args = parser.parse_known_args(argv)
  
  pipeline_options = PipelineOptions(pipeline_args)
  with beam.Pipeline(options=pipeline_options) as p:

    (p
      | 'read' >> ReadFromText(known_args.input)
      | 'copy' >> WriteToText(known_args.output))


if __name__ == '__main__':
  run()
