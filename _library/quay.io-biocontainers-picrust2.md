---
layout: container
name:  "quay.io/biocontainers/picrust2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/picrust2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/picrust2/container.yaml"
updated_at: "2025-03-24 03:17:33.170604"
latest: "2.6.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/picrust2"
aliases:
 - "add_descriptions.py"
 - "convert_table.py"
 - "epa-ng"
 - "gappa"
 - "hmmc2"
 - "hmmerfm-exactmatch"
 - "hsp.py"
 - "metagenome_pipeline.py"
 - "pathway_pipeline.py"
 - "picrust2_pipeline.py"
 - "place_seqs.py"
 - "print_picrust2_config.py"
 - "run-sepp.sh"
 - "run_abundance.py"
 - "run_sepp.py"
 - "run_tipp.py"
 - "run_tipp_tool.py"
 - "run_upp.py"
 - "seppJsonMerger.jar"
 - "shuffle_predictions.py"
 - "split_sequences.py"
 - "coverage"
 - "guppy"
 - "pplacer"
 - "biom"
 - "dendropy-format"
 - "sumlabels.py"
 - "sumtrees.py"
 - "py.test"
 - "pytest"
 - "glpsol"
versions:
 - "2.5.0--pyhdfd78af_0"
 - "2.5.1--pyhdfd78af_0"
 - "2.5.2--pyhdfd78af_0"
 - "2.5.3--pyhdfd78af_0"
 - "2.6.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for picrust2"
config: {"url": "https://biocontainers.pro/tools/picrust2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for picrust2", "latest": {"2.6.0--pyhdfd78af_0": "sha256:2c46e2dcddf896efd4becdb0305cca5be8e391a8c68e03e644ca54679b7f60ee"}, "tags": {"2.5.0--pyhdfd78af_0": "sha256:067e227408ccc5618708756109a29e04c02750b7fe5c23d236db34f6d018de2c", "2.5.1--pyhdfd78af_0": "sha256:47f5b99ff3c667fb38ebc772693594358813d30d3bcfe4cb95b85986ca0bbaad", "2.5.2--pyhdfd78af_0": "sha256:23765ee45bc261b225576a283171c39737f95722896570a1f24b181857fbc29f", "2.5.3--pyhdfd78af_0": "sha256:45c59112a4eef4d1671449b19e03ee99948fced6149c72d2a349775f075e290d", "2.6.0--pyhdfd78af_0": "sha256:2c46e2dcddf896efd4becdb0305cca5be8e391a8c68e03e644ca54679b7f60ee"}, "docker": "quay.io/biocontainers/picrust2", "aliases": {"add_descriptions.py": "/usr/local/bin/add_descriptions.py", "convert_table.py": "/usr/local/bin/convert_table.py", "epa-ng": "/usr/local/bin/epa-ng", "gappa": "/usr/local/bin/gappa", "hmmc2": "/usr/local/bin/hmmc2", "hmmerfm-exactmatch": "/usr/local/bin/hmmerfm-exactmatch", "hsp.py": "/usr/local/bin/hsp.py", "metagenome_pipeline.py": "/usr/local/bin/metagenome_pipeline.py", "pathway_pipeline.py": "/usr/local/bin/pathway_pipeline.py", "picrust2_pipeline.py": "/usr/local/bin/picrust2_pipeline.py", "place_seqs.py": "/usr/local/bin/place_seqs.py", "print_picrust2_config.py": "/usr/local/bin/print_picrust2_config.py", "run-sepp.sh": "/usr/local/bin/run-sepp.sh", "run_abundance.py": "/usr/local/bin/run_abundance.py", "run_sepp.py": "/usr/local/bin/run_sepp.py", "run_tipp.py": "/usr/local/bin/run_tipp.py", "run_tipp_tool.py": "/usr/local/bin/run_tipp_tool.py", "run_upp.py": "/usr/local/bin/run_upp.py", "seppJsonMerger.jar": "/usr/local/bin/seppJsonMerger.jar", "shuffle_predictions.py": "/usr/local/bin/shuffle_predictions.py", "split_sequences.py": "/usr/local/bin/split_sequences.py", "coverage": "/usr/local/bin/coverage", "guppy": "/usr/local/bin/guppy", "pplacer": "/usr/local/bin/pplacer", "biom": "/usr/local/bin/biom", "dendropy-format": "/usr/local/bin/dendropy-format", "sumlabels.py": "/usr/local/bin/sumlabels.py", "sumtrees.py": "/usr/local/bin/sumtrees.py", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/picrust2.
shpc-registry automated BioContainers addition for picrust2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/picrust2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/picrust2:2.6.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/picrust2/2.6.0--pyhdfd78af_0
$ module help quay.io/biocontainers/picrust2/2.6.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### picrust2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### picrust2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### picrust2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### picrust2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### picrust2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### picrust2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add_descriptions.py

```bash
$ singularity exec <container> /usr/local/bin/add_descriptions.py
$ podman run --it --rm --entrypoint /usr/local/bin/add_descriptions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_descriptions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_table.py

```bash
$ singularity exec <container> /usr/local/bin/convert_table.py
$ podman run --it --rm --entrypoint /usr/local/bin/convert_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### epa-ng

```bash
$ singularity exec <container> /usr/local/bin/epa-ng
$ podman run --it --rm --entrypoint /usr/local/bin/epa-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epa-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gappa

```bash
$ singularity exec <container> /usr/local/bin/gappa
$ podman run --it --rm --entrypoint /usr/local/bin/gappa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gappa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmc2

```bash
$ singularity exec <container> /usr/local/bin/hmmc2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmerfm-exactmatch

```bash
$ singularity exec <container> /usr/local/bin/hmmerfm-exactmatch
$ podman run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hsp.py

```bash
$ singularity exec <container> /usr/local/bin/hsp.py
$ podman run --it --rm --entrypoint /usr/local/bin/hsp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hsp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metagenome_pipeline.py

```bash
$ singularity exec <container> /usr/local/bin/metagenome_pipeline.py
$ podman run --it --rm --entrypoint /usr/local/bin/metagenome_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metagenome_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathway_pipeline.py

```bash
$ singularity exec <container> /usr/local/bin/pathway_pipeline.py
$ podman run --it --rm --entrypoint /usr/local/bin/pathway_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathway_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### picrust2_pipeline.py

```bash
$ singularity exec <container> /usr/local/bin/picrust2_pipeline.py
$ podman run --it --rm --entrypoint /usr/local/bin/picrust2_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/picrust2_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### place_seqs.py

```bash
$ singularity exec <container> /usr/local/bin/place_seqs.py
$ podman run --it --rm --entrypoint /usr/local/bin/place_seqs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/place_seqs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### print_picrust2_config.py

```bash
$ singularity exec <container> /usr/local/bin/print_picrust2_config.py
$ podman run --it --rm --entrypoint /usr/local/bin/print_picrust2_config.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/print_picrust2_config.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-sepp.sh

```bash
$ singularity exec <container> /usr/local/bin/run-sepp.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run-sepp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-sepp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_abundance.py

```bash
$ singularity exec <container> /usr/local/bin/run_abundance.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_abundance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_abundance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_sepp.py

```bash
$ singularity exec <container> /usr/local/bin/run_sepp.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_sepp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_sepp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_tipp.py

```bash
$ singularity exec <container> /usr/local/bin/run_tipp.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_tipp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_tipp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_tipp_tool.py

```bash
$ singularity exec <container> /usr/local/bin/run_tipp_tool.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_tipp_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_tipp_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_upp.py

```bash
$ singularity exec <container> /usr/local/bin/run_upp.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_upp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_upp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seppJsonMerger.jar

```bash
$ singularity exec <container> /usr/local/bin/seppJsonMerger.jar
$ podman run --it --rm --entrypoint /usr/local/bin/seppJsonMerger.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seppJsonMerger.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shuffle_predictions.py

```bash
$ singularity exec <container> /usr/local/bin/shuffle_predictions.py
$ podman run --it --rm --entrypoint /usr/local/bin/shuffle_predictions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shuffle_predictions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_sequences.py

```bash
$ singularity exec <container> /usr/local/bin/split_sequences.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_sequences.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_sequences.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage

```bash
$ singularity exec <container> /usr/local/bin/coverage
$ podman run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guppy

```bash
$ singularity exec <container> /usr/local/bin/guppy
$ podman run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pplacer

```bash
$ singularity exec <container> /usr/local/bin/pplacer
$ podman run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biom

```bash
$ singularity exec <container> /usr/local/bin/biom
$ podman run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumlabels.py

```bash
$ singularity exec <container> /usr/local/bin/sumlabels.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumtrees.py

```bash
$ singularity exec <container> /usr/local/bin/sumtrees.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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