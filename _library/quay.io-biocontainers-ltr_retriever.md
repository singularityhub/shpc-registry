---
layout: container
name:  "quay.io/biocontainers/ltr_retriever"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ltr_retriever/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ltr_retriever/container.yaml"
updated_at: "2022-10-29 05:43:56.767926"
latest: "2.9.0--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/ltr_retriever"
aliases:
 - "LAI"
 - "LTR_retriever"
 - "RM2Bed.py"
 - "buildRMLibFromEMBL.pl"
 - "buildSummary.pl"
 - "convert_MGEScan3.0.pl"
 - "convert_ltr_struc.pl"
 - "convert_ltrdetector.pl"
 - "queryRepeatDatabase.pl"
 - "queryTaxonomyDatabase.pl"
 - "wublastToCrossmatch.pl"
 - "CA.pm"
 - "DateRepeats"
 - "DupMasker"
 - "FET.pl"
 - "ProcessRepeats"
 - "RepeatMasker"
 - "RepeatProteinMask"
 - "accn-at-a-time"
 - "alimask"
 - "amino-acid-composition"
versions:
 - "2.9.0--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for ltr_retriever"
config: {"url": "https://biocontainers.pro/tools/ltr_retriever", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ltr_retriever", "latest": {"2.9.0--hdfd78af_1": "sha256:881fbf91a576048b71c7f9328609e4a9554bbe283400af3931a25250206c2b58"}, "tags": {"2.9.0--hdfd78af_1": "sha256:881fbf91a576048b71c7f9328609e4a9554bbe283400af3931a25250206c2b58"}, "docker": "quay.io/biocontainers/ltr_retriever", "aliases": {"LAI": "/usr/local/bin/LAI", "LTR_retriever": "/usr/local/bin/LTR_retriever", "RM2Bed.py": "/usr/local/bin/RM2Bed.py", "buildRMLibFromEMBL.pl": "/usr/local/bin/buildRMLibFromEMBL.pl", "buildSummary.pl": "/usr/local/bin/buildSummary.pl", "convert_MGEScan3.0.pl": "/usr/local/bin/convert_MGEScan3.0.pl", "convert_ltr_struc.pl": "/usr/local/bin/convert_ltr_struc.pl", "convert_ltrdetector.pl": "/usr/local/bin/convert_ltrdetector.pl", "queryRepeatDatabase.pl": "/usr/local/bin/queryRepeatDatabase.pl", "queryTaxonomyDatabase.pl": "/usr/local/bin/queryTaxonomyDatabase.pl", "wublastToCrossmatch.pl": "/usr/local/bin/wublastToCrossmatch.pl", "CA.pm": "/usr/local/bin/CA.pm", "DateRepeats": "/usr/local/bin/DateRepeats", "DupMasker": "/usr/local/bin/DupMasker", "FET.pl": "/usr/local/bin/FET.pl", "ProcessRepeats": "/usr/local/bin/ProcessRepeats", "RepeatMasker": "/usr/local/bin/RepeatMasker", "RepeatProteinMask": "/usr/local/bin/RepeatProteinMask", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "alimask": "/usr/local/bin/alimask", "amino-acid-composition": "/usr/local/bin/amino-acid-composition"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ltr_retriever.
shpc-registry automated BioContainers addition for ltr_retriever
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ltr_retriever
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ltr_retriever:2.9.0--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ltr_retriever/2.9.0--hdfd78af_1
$ module help quay.io/biocontainers/ltr_retriever/2.9.0--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ltr_retriever-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ltr_retriever-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ltr_retriever-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ltr_retriever-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ltr_retriever-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ltr_retriever-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LAI

```bash
$ singularity exec <container> /usr/local/bin/LAI
$ podman run --it --rm --entrypoint /usr/local/bin/LAI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LTR_retriever

```bash
$ singularity exec <container> /usr/local/bin/LTR_retriever
$ podman run --it --rm --entrypoint /usr/local/bin/LTR_retriever   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LTR_retriever   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RM2Bed.py

```bash
$ singularity exec <container> /usr/local/bin/RM2Bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/RM2Bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RM2Bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildRMLibFromEMBL.pl

```bash
$ singularity exec <container> /usr/local/bin/buildRMLibFromEMBL.pl
$ podman run --it --rm --entrypoint /usr/local/bin/buildRMLibFromEMBL.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildRMLibFromEMBL.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildSummary.pl

```bash
$ singularity exec <container> /usr/local/bin/buildSummary.pl
$ podman run --it --rm --entrypoint /usr/local/bin/buildSummary.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildSummary.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_MGEScan3.0.pl

```bash
$ singularity exec <container> /usr/local/bin/convert_MGEScan3.0.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convert_MGEScan3.0.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_MGEScan3.0.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_ltr_struc.pl

```bash
$ singularity exec <container> /usr/local/bin/convert_ltr_struc.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convert_ltr_struc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_ltr_struc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_ltrdetector.pl

```bash
$ singularity exec <container> /usr/local/bin/convert_ltrdetector.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convert_ltrdetector.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_ltrdetector.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### queryRepeatDatabase.pl

```bash
$ singularity exec <container> /usr/local/bin/queryRepeatDatabase.pl
$ podman run --it --rm --entrypoint /usr/local/bin/queryRepeatDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/queryRepeatDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### queryTaxonomyDatabase.pl

```bash
$ singularity exec <container> /usr/local/bin/queryTaxonomyDatabase.pl
$ podman run --it --rm --entrypoint /usr/local/bin/queryTaxonomyDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/queryTaxonomyDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wublastToCrossmatch.pl

```bash
$ singularity exec <container> /usr/local/bin/wublastToCrossmatch.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wublastToCrossmatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wublastToCrossmatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DateRepeats

```bash
$ singularity exec <container> /usr/local/bin/DateRepeats
$ podman run --it --rm --entrypoint /usr/local/bin/DateRepeats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DateRepeats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DupMasker

```bash
$ singularity exec <container> /usr/local/bin/DupMasker
$ podman run --it --rm --entrypoint /usr/local/bin/DupMasker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DupMasker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FET.pl

```bash
$ singularity exec <container> /usr/local/bin/FET.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ProcessRepeats

```bash
$ singularity exec <container> /usr/local/bin/ProcessRepeats
$ podman run --it --rm --entrypoint /usr/local/bin/ProcessRepeats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ProcessRepeats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RepeatMasker

```bash
$ singularity exec <container> /usr/local/bin/RepeatMasker
$ podman run --it --rm --entrypoint /usr/local/bin/RepeatMasker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RepeatMasker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RepeatProteinMask

```bash
$ singularity exec <container> /usr/local/bin/RepeatProteinMask
$ podman run --it --rm --entrypoint /usr/local/bin/RepeatProteinMask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RepeatProteinMask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accn-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/accn-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amino-acid-composition

```bash
$ singularity exec <container> /usr/local/bin/amino-acid-composition
$ podman run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
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