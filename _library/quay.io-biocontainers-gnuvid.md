---
layout: container
name:  "quay.io/biocontainers/gnuvid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gnuvid/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gnuvid/container.yaml"
updated_at: "2024-06-13 03:16:33.627394"
latest: "2.4--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/gnuvid"
aliases:
 - "Clonal_complex_assigner.py"
 - "Extract_US_genomes.py"
 - "Extract_fasta_sequence_blast_report.py"
 - "GNUVID.py"
 - "GNUVID_CCs_summary.py"
 - "GNUVID_FASTA_divider.py"
 - "GNUVID_Post_CC_processor.py"
 - "GNUVID_Post_Training.py"
 - "GNUVID_Predict.py"
 - "GNUVID_Subsample_STs.py"
 - "GNUVID_Training.py"
 - "GNUVID_database_customizer.py"
 - "GNUVID_preprocessor.py"
 - "GNUVID_update_db.py"
 - "Metadata_piechart.py"
 - "Temporal_plot_Introductions_Importations.py"
 - "gofasta"
 - "filter-table"
 - "spdi2prod"
 - "mafft-sparsecore.rb"
 - "einsi"
 - "fftns"
 - "fftnsi"
 - "ginsi"
 - "linsi"
 - "mafft-distance"
 - "mafft-einsi"
versions:
 - "2.4--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for gnuvid"
config: {"url": "https://biocontainers.pro/tools/gnuvid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gnuvid", "latest": {"2.4--hdfd78af_0": "sha256:42db7365c34d8bc01d6f2ed63e40301c01eb95af76c6acb8dd203cb152b89391"}, "tags": {"2.4--hdfd78af_0": "sha256:42db7365c34d8bc01d6f2ed63e40301c01eb95af76c6acb8dd203cb152b89391"}, "docker": "quay.io/biocontainers/gnuvid", "aliases": {"Clonal_complex_assigner.py": "/usr/local/bin/Clonal_complex_assigner.py", "Extract_US_genomes.py": "/usr/local/bin/Extract_US_genomes.py", "Extract_fasta_sequence_blast_report.py": "/usr/local/bin/Extract_fasta_sequence_blast_report.py", "GNUVID.py": "/usr/local/bin/GNUVID.py", "GNUVID_CCs_summary.py": "/usr/local/bin/GNUVID_CCs_summary.py", "GNUVID_FASTA_divider.py": "/usr/local/bin/GNUVID_FASTA_divider.py", "GNUVID_Post_CC_processor.py": "/usr/local/bin/GNUVID_Post_CC_processor.py", "GNUVID_Post_Training.py": "/usr/local/bin/GNUVID_Post_Training.py", "GNUVID_Predict.py": "/usr/local/bin/GNUVID_Predict.py", "GNUVID_Subsample_STs.py": "/usr/local/bin/GNUVID_Subsample_STs.py", "GNUVID_Training.py": "/usr/local/bin/GNUVID_Training.py", "GNUVID_database_customizer.py": "/usr/local/bin/GNUVID_database_customizer.py", "GNUVID_preprocessor.py": "/usr/local/bin/GNUVID_preprocessor.py", "GNUVID_update_db.py": "/usr/local/bin/GNUVID_update_db.py", "Metadata_piechart.py": "/usr/local/bin/Metadata_piechart.py", "Temporal_plot_Introductions_Importations.py": "/usr/local/bin/Temporal_plot_Introductions_Importations.py", "gofasta": "/usr/local/bin/gofasta", "filter-table": "/usr/local/bin/filter-table", "spdi2prod": "/usr/local/bin/spdi2prod", "mafft-sparsecore.rb": "/usr/local/bin/mafft-sparsecore.rb", "einsi": "/usr/local/bin/einsi", "fftns": "/usr/local/bin/fftns", "fftnsi": "/usr/local/bin/fftnsi", "ginsi": "/usr/local/bin/ginsi", "linsi": "/usr/local/bin/linsi", "mafft-distance": "/usr/local/bin/mafft-distance", "mafft-einsi": "/usr/local/bin/mafft-einsi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gnuvid.
shpc-registry automated BioContainers addition for gnuvid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gnuvid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gnuvid:2.4--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gnuvid/2.4--hdfd78af_0
$ module help quay.io/biocontainers/gnuvid/2.4--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gnuvid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gnuvid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gnuvid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gnuvid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gnuvid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gnuvid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Clonal_complex_assigner.py

```bash
$ singularity exec <container> /usr/local/bin/Clonal_complex_assigner.py
$ podman run --it --rm --entrypoint /usr/local/bin/Clonal_complex_assigner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Clonal_complex_assigner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Extract_US_genomes.py

```bash
$ singularity exec <container> /usr/local/bin/Extract_US_genomes.py
$ podman run --it --rm --entrypoint /usr/local/bin/Extract_US_genomes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Extract_US_genomes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Extract_fasta_sequence_blast_report.py

```bash
$ singularity exec <container> /usr/local/bin/Extract_fasta_sequence_blast_report.py
$ podman run --it --rm --entrypoint /usr/local/bin/Extract_fasta_sequence_blast_report.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Extract_fasta_sequence_blast_report.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GNUVID.py

```bash
$ singularity exec <container> /usr/local/bin/GNUVID.py
$ podman run --it --rm --entrypoint /usr/local/bin/GNUVID.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GNUVID.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GNUVID_CCs_summary.py

```bash
$ singularity exec <container> /usr/local/bin/GNUVID_CCs_summary.py
$ podman run --it --rm --entrypoint /usr/local/bin/GNUVID_CCs_summary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GNUVID_CCs_summary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GNUVID_FASTA_divider.py

```bash
$ singularity exec <container> /usr/local/bin/GNUVID_FASTA_divider.py
$ podman run --it --rm --entrypoint /usr/local/bin/GNUVID_FASTA_divider.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GNUVID_FASTA_divider.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GNUVID_Post_CC_processor.py

```bash
$ singularity exec <container> /usr/local/bin/GNUVID_Post_CC_processor.py
$ podman run --it --rm --entrypoint /usr/local/bin/GNUVID_Post_CC_processor.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GNUVID_Post_CC_processor.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GNUVID_Post_Training.py

```bash
$ singularity exec <container> /usr/local/bin/GNUVID_Post_Training.py
$ podman run --it --rm --entrypoint /usr/local/bin/GNUVID_Post_Training.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GNUVID_Post_Training.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GNUVID_Predict.py

```bash
$ singularity exec <container> /usr/local/bin/GNUVID_Predict.py
$ podman run --it --rm --entrypoint /usr/local/bin/GNUVID_Predict.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GNUVID_Predict.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GNUVID_Subsample_STs.py

```bash
$ singularity exec <container> /usr/local/bin/GNUVID_Subsample_STs.py
$ podman run --it --rm --entrypoint /usr/local/bin/GNUVID_Subsample_STs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GNUVID_Subsample_STs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GNUVID_Training.py

```bash
$ singularity exec <container> /usr/local/bin/GNUVID_Training.py
$ podman run --it --rm --entrypoint /usr/local/bin/GNUVID_Training.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GNUVID_Training.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GNUVID_database_customizer.py

```bash
$ singularity exec <container> /usr/local/bin/GNUVID_database_customizer.py
$ podman run --it --rm --entrypoint /usr/local/bin/GNUVID_database_customizer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GNUVID_database_customizer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GNUVID_preprocessor.py

```bash
$ singularity exec <container> /usr/local/bin/GNUVID_preprocessor.py
$ podman run --it --rm --entrypoint /usr/local/bin/GNUVID_preprocessor.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GNUVID_preprocessor.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GNUVID_update_db.py

```bash
$ singularity exec <container> /usr/local/bin/GNUVID_update_db.py
$ podman run --it --rm --entrypoint /usr/local/bin/GNUVID_update_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GNUVID_update_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Metadata_piechart.py

```bash
$ singularity exec <container> /usr/local/bin/Metadata_piechart.py
$ podman run --it --rm --entrypoint /usr/local/bin/Metadata_piechart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Metadata_piechart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Temporal_plot_Introductions_Importations.py

```bash
$ singularity exec <container> /usr/local/bin/Temporal_plot_Introductions_Importations.py
$ podman run --it --rm --entrypoint /usr/local/bin/Temporal_plot_Introductions_Importations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Temporal_plot_Introductions_Importations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gofasta

```bash
$ singularity exec <container> /usr/local/bin/gofasta
$ podman run --it --rm --entrypoint /usr/local/bin/gofasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gofasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-table

```bash
$ singularity exec <container> /usr/local/bin/filter-table
$ podman run --it --rm --entrypoint /usr/local/bin/filter-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spdi2prod

```bash
$ singularity exec <container> /usr/local/bin/spdi2prod
$ podman run --it --rm --entrypoint /usr/local/bin/spdi2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spdi2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-sparsecore.rb

```bash
$ singularity exec <container> /usr/local/bin/mafft-sparsecore.rb
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### einsi

```bash
$ singularity exec <container> /usr/local/bin/einsi
$ podman run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftns

```bash
$ singularity exec <container> /usr/local/bin/fftns
$ podman run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftnsi

```bash
$ singularity exec <container> /usr/local/bin/fftnsi
$ podman run --it --rm --entrypoint /usr/local/bin/fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ginsi

```bash
$ singularity exec <container> /usr/local/bin/ginsi
$ podman run --it --rm --entrypoint /usr/local/bin/ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linsi

```bash
$ singularity exec <container> /usr/local/bin/linsi
$ podman run --it --rm --entrypoint /usr/local/bin/linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-distance

```bash
$ singularity exec <container> /usr/local/bin/mafft-distance
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-distance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-distance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-einsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-einsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)