---
layout: container
name:  "quay.io/biocontainers/galaxy-data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/galaxy-data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/galaxy-data/container.yaml"
updated_at: "2024-03-27 03:00:23.590802"
latest: "22.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/galaxy-data"
aliases:
 - "bagit.py"
 - "bagit_profile.py"
 - "bdbag"
 - "bdbag-utils"
 - "cheetah"
 - "cheetah-analyze"
 - "cheetah-compile"
 - "galaxy-build-objects"
 - "galaxy-manage-db"
 - "gx-fastq-combiner"
 - "gx-fastq-filter"
 - "gx-fastq-groomer"
 - "gx-fastq-manipulation"
 - "gx-fastq-masker-by-quality"
 - "gx-fastq-paired-end-deinterlacer"
 - "gx-fastq-paired-end-interlacer"
 - "gx-fastq-paired-end-joiner"
 - "gx-fastq-paired-end-splitter"
 - "gx-fastq-stats"
 - "gx-fastq-to-fasta"
 - "gx-fastq-to-tabular"
 - "gx-fastq-trimmer"
 - "gx-fastq-trimmer-by-quality"
 - "migrate"
 - "migrate-repository"
 - "sqlformat"
 - "pbr"
 - "docutils"
 - "pybabel"
 - "aggregate_scores_in_intervals.py"
 - "align_print_template.py"
 - "axt_extract_ranges.py"
 - "axt_to_fasta.py"
 - "axt_to_lav.py"
 - "axt_to_maf.py"
 - "bed_bigwig_profile.py"
versions:
 - "22.1.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for galaxy-data"
config: {"url": "https://biocontainers.pro/tools/galaxy-data", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for galaxy-data", "latest": {"22.1.1--pyhdfd78af_0": "sha256:0493f9c28131ca24f6ffdd49773249c2fd25f6427928625d10410bddcc37a3e7"}, "tags": {"22.1.1--pyhdfd78af_0": "sha256:0493f9c28131ca24f6ffdd49773249c2fd25f6427928625d10410bddcc37a3e7"}, "docker": "quay.io/biocontainers/galaxy-data", "aliases": {"bagit.py": "/usr/local/bin/bagit.py", "bagit_profile.py": "/usr/local/bin/bagit_profile.py", "bdbag": "/usr/local/bin/bdbag", "bdbag-utils": "/usr/local/bin/bdbag-utils", "cheetah": "/usr/local/bin/cheetah", "cheetah-analyze": "/usr/local/bin/cheetah-analyze", "cheetah-compile": "/usr/local/bin/cheetah-compile", "galaxy-build-objects": "/usr/local/bin/galaxy-build-objects", "galaxy-manage-db": "/usr/local/bin/galaxy-manage-db", "gx-fastq-combiner": "/usr/local/bin/gx-fastq-combiner", "gx-fastq-filter": "/usr/local/bin/gx-fastq-filter", "gx-fastq-groomer": "/usr/local/bin/gx-fastq-groomer", "gx-fastq-manipulation": "/usr/local/bin/gx-fastq-manipulation", "gx-fastq-masker-by-quality": "/usr/local/bin/gx-fastq-masker-by-quality", "gx-fastq-paired-end-deinterlacer": "/usr/local/bin/gx-fastq-paired-end-deinterlacer", "gx-fastq-paired-end-interlacer": "/usr/local/bin/gx-fastq-paired-end-interlacer", "gx-fastq-paired-end-joiner": "/usr/local/bin/gx-fastq-paired-end-joiner", "gx-fastq-paired-end-splitter": "/usr/local/bin/gx-fastq-paired-end-splitter", "gx-fastq-stats": "/usr/local/bin/gx-fastq-stats", "gx-fastq-to-fasta": "/usr/local/bin/gx-fastq-to-fasta", "gx-fastq-to-tabular": "/usr/local/bin/gx-fastq-to-tabular", "gx-fastq-trimmer": "/usr/local/bin/gx-fastq-trimmer", "gx-fastq-trimmer-by-quality": "/usr/local/bin/gx-fastq-trimmer-by-quality", "migrate": "/usr/local/bin/migrate", "migrate-repository": "/usr/local/bin/migrate-repository", "sqlformat": "/usr/local/bin/sqlformat", "pbr": "/usr/local/bin/pbr", "docutils": "/usr/local/bin/docutils", "pybabel": "/usr/local/bin/pybabel", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py", "axt_to_fasta.py": "/usr/local/bin/axt_to_fasta.py", "axt_to_lav.py": "/usr/local/bin/axt_to_lav.py", "axt_to_maf.py": "/usr/local/bin/axt_to_maf.py", "bed_bigwig_profile.py": "/usr/local/bin/bed_bigwig_profile.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/galaxy-data.
shpc-registry automated BioContainers addition for galaxy-data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/galaxy-data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/galaxy-data:22.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/galaxy-data/22.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/galaxy-data/22.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### galaxy-data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### galaxy-data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### galaxy-data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### galaxy-data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### galaxy-data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### galaxy-data-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bagit.py

```bash
$ singularity exec <container> /usr/local/bin/bagit.py
$ podman run --it --rm --entrypoint /usr/local/bin/bagit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bagit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bagit_profile.py

```bash
$ singularity exec <container> /usr/local/bin/bagit_profile.py
$ podman run --it --rm --entrypoint /usr/local/bin/bagit_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bagit_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdbag

```bash
$ singularity exec <container> /usr/local/bin/bdbag
$ podman run --it --rm --entrypoint /usr/local/bin/bdbag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdbag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdbag-utils

```bash
$ singularity exec <container> /usr/local/bin/bdbag-utils
$ podman run --it --rm --entrypoint /usr/local/bin/bdbag-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdbag-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheetah

```bash
$ singularity exec <container> /usr/local/bin/cheetah
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheetah-analyze

```bash
$ singularity exec <container> /usr/local/bin/cheetah-analyze
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheetah-compile

```bash
$ singularity exec <container> /usr/local/bin/cheetah-compile
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah-compile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah-compile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### galaxy-build-objects

```bash
$ singularity exec <container> /usr/local/bin/galaxy-build-objects
$ podman run --it --rm --entrypoint /usr/local/bin/galaxy-build-objects   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/galaxy-build-objects   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### galaxy-manage-db

```bash
$ singularity exec <container> /usr/local/bin/galaxy-manage-db
$ podman run --it --rm --entrypoint /usr/local/bin/galaxy-manage-db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/galaxy-manage-db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-combiner

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-combiner
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-combiner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-combiner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-filter

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-filter
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-groomer

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-groomer
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-groomer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-groomer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-manipulation

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-manipulation
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-manipulation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-manipulation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-masker-by-quality

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-masker-by-quality
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-masker-by-quality   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-masker-by-quality   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-paired-end-deinterlacer

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-paired-end-deinterlacer
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-deinterlacer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-deinterlacer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-paired-end-interlacer

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-paired-end-interlacer
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-interlacer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-interlacer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-paired-end-joiner

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-paired-end-joiner
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-joiner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-joiner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-paired-end-splitter

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-paired-end-splitter
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-splitter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-splitter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-stats

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-stats
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-to-fasta

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-to-fasta
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-to-tabular

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-to-tabular
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-to-tabular   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-to-tabular   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-trimmer

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-trimmer
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-trimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-trimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-trimmer-by-quality

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-trimmer-by-quality
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-trimmer-by-quality   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-trimmer-by-quality   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### migrate

```bash
$ singularity exec <container> /usr/local/bin/migrate
$ podman run --it --rm --entrypoint /usr/local/bin/migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### migrate-repository

```bash
$ singularity exec <container> /usr/local/bin/migrate-repository
$ podman run --it --rm --entrypoint /usr/local/bin/migrate-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/migrate-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sqlformat

```bash
$ singularity exec <container> /usr/local/bin/sqlformat
$ podman run --it --rm --entrypoint /usr/local/bin/sqlformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sqlformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbr

```bash
$ singularity exec <container> /usr/local/bin/pbr
$ podman run --it --rm --entrypoint /usr/local/bin/pbr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybabel

```bash
$ singularity exec <container> /usr/local/bin/pybabel
$ podman run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_scores_in_intervals.py

```bash
$ singularity exec <container> /usr/local/bin/aggregate_scores_in_intervals.py
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align_print_template.py

```bash
$ singularity exec <container> /usr/local/bin/align_print_template.py
$ podman run --it --rm --entrypoint /usr/local/bin/align_print_template.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align_print_template.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_extract_ranges.py

```bash
$ singularity exec <container> /usr/local/bin/axt_extract_ranges.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_extract_ranges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_extract_ranges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_lav.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_lav.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_lav.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_lav.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_maf.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_maf.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_maf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_maf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_bigwig_profile.py

```bash
$ singularity exec <container> /usr/local/bin/bed_bigwig_profile.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_bigwig_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_bigwig_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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