'''The stack dataset'''

import tensorflow_datasets as tfds
import os


class Builder(tfds.core.GeneratorBasedBuilder):
  '''DatasetBuilder for the Stack dataset.'''

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  MANUAL_DOWNLOAD_INSTRUCTIONS = """
  Place the '.jsonl' files in the `manual_dir/`.
  """
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def _info(self) -> tfds.core.DatasetInfo:
    '''Returns the dataset metadata.'''
    # TODO(Redpajama_Test): Specifies the tfds.core.DatasetInfo object
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'text': tfds.features.Text(),
            'meta': tfds.features.Text(),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=None,  # Set to `None` to disable
        homepage='https://dataset-homepage/',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    '''Returns SplitGenerators.'''
    from etils import epath
    def find_parquet_files(directory): 
        jsonl_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if file.endswith('.parquet'):
                    jsonl_files.append(file_path)
        return jsonl_files
    parquet_files = find_parquet_files(dl_manager.manual_dir)
    parquet_files = [epath.Path(path) for path in sorted(parquet_files)]  
    print('parquet files num:', len(parquet_files))
    return {
        'train': self._generate_examples(parquet_files)
    }

  def _generate_examples(self, files):
    '''Yields examples.'''
    import traceback
    import fastparquet
    key = 0
    for file in files:
        pf = fastparquet.ParquetFile(file)
        df = pf.to_pandas()
        for _, row in df.iterrows():
            try:
                yield key, {
                    'text': row['content'],
                    'meta': str(row.drop(['content']).items())
                }
                key += 1
            except Exception as e:
                print(f'Path: {file}')
                print(f'Row: {row}')
                traceback.print_exc()
                raise e
