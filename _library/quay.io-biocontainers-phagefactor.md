---
layout: container
name:  "quay.io/biocontainers/phagefactor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phagefactor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phagefactor/container.yaml"
updated_at: "2026-11-08 09:14:37.725306"
latest: "1.2.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/phagefactor"
aliases:
 - "create_custom_hmm.py"
 - "dnaapler"
 - "genbank.py"
 - "generate-slurm-partition-config"
 - "install_databases.py"
 - "phagefactor"
 - "phanotate.py"
 - "pharokka"
 - "pharokka.py"
 - "pharokka_multiplotter.py"
 - "pharokka_plotter.py"
 - "pharokka_proteins.py"
 - "phold"
 - "pyrodigal-rv"
 - "spm_decode"
 - "spm_encode"
 - "spm_export_vocab"
 - "spm_normalize"
 - "spm_train"
 - "foldseek"
 - "MitoHighConfidenceFilter"
 - "datasets-cli"
 - "pyrodigal-gv"
 - "transformers"
 - "black"
 - "blackd"
 - "isort-identify-imports"
 - "isort"
 - "gawk-5.4.1"
 - "EukHighConfidenceFilter"
 - "covels-SE"
 - "coves-SE"
 - "eufindtRNA"
 - "fasta2gsi"
 - "hf"
 - "protoc-28.3.0"
 - "sstofa"
 - "tRNAscan-SE"
 - "tRNAscan-SE.conf"
 - "trnascan-1.4"
 - "coverage"
 - "tiny-agents"
 - "huggingface-cli"
 - "minced"
versions:
 - "1.2.0--hdfd78af_0"
description: "singularity registry hpc automated addition for phagefactor"
config: {"url": "https://biocontainers.pro/tools/phagefactor", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for phagefactor", "latest": {"1.2.0--hdfd78af_0": "sha256:f04c48d8d9b72fd6de27526e3015617d3d04bc22bbbc51fe717a545ebb1f13c7"}, "tags": {"1.2.0--hdfd78af_0": "sha256:f04c48d8d9b72fd6de27526e3015617d3d04bc22bbbc51fe717a545ebb1f13c7"}, "docker": "quay.io/biocontainers/phagefactor", "aliases": {"create_custom_hmm.py": "/usr/local/bin/create_custom_hmm.py", "dnaapler": "/usr/local/bin/dnaapler", "genbank.py": "/usr/local/bin/genbank.py", "generate-slurm-partition-config": "/usr/local/bin/generate-slurm-partition-config", "install_databases.py": "/usr/local/bin/install_databases.py", "phagefactor": "/usr/local/bin/phagefactor", "phanotate.py": "/usr/local/bin/phanotate.py", "pharokka": "/usr/local/bin/pharokka", "pharokka.py": "/usr/local/bin/pharokka.py", "pharokka_multiplotter.py": "/usr/local/bin/pharokka_multiplotter.py", "pharokka_plotter.py": "/usr/local/bin/pharokka_plotter.py", "pharokka_proteins.py": "/usr/local/bin/pharokka_proteins.py", "phold": "/usr/local/bin/phold", "pyrodigal-rv": "/usr/local/bin/pyrodigal-rv", "spm_decode": "/usr/local/bin/spm_decode", "spm_encode": "/usr/local/bin/spm_encode", "spm_export_vocab": "/usr/local/bin/spm_export_vocab", "spm_normalize": "/usr/local/bin/spm_normalize", "spm_train": "/usr/local/bin/spm_train", "foldseek": "/usr/local/bin/foldseek", "MitoHighConfidenceFilter": "/usr/local/bin/MitoHighConfidenceFilter", "datasets-cli": "/usr/local/bin/datasets-cli", "pyrodigal-gv": "/usr/local/bin/pyrodigal-gv", "transformers": "/usr/local/bin/transformers", "black": "/usr/local/bin/black", "blackd": "/usr/local/bin/blackd", "isort-identify-imports": "/usr/local/bin/isort-identify-imports", "isort": "/usr/local/bin/isort", "gawk-5.4.1": "/usr/local/bin/gawk-5.4.1", "EukHighConfidenceFilter": "/usr/local/bin/EukHighConfidenceFilter", "covels-SE": "/usr/local/bin/covels-SE", "coves-SE": "/usr/local/bin/coves-SE", "eufindtRNA": "/usr/local/bin/eufindtRNA", "fasta2gsi": "/usr/local/bin/fasta2gsi", "hf": "/usr/local/bin/hf", "protoc-28.3.0": "/usr/local/bin/protoc-28.3.0", "sstofa": "/usr/local/bin/sstofa", "tRNAscan-SE": "/usr/local/bin/tRNAscan-SE", "tRNAscan-SE.conf": "/usr/local/bin/tRNAscan-SE.conf", "trnascan-1.4": "/usr/local/bin/trnascan-1.4", "coverage": "/usr/local/bin/coverage", "tiny-agents": "/usr/local/bin/tiny-agents", "huggingface-cli": "/usr/local/bin/huggingface-cli", "minced": "/usr/local/bin/minced"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phagefactor.
singularity registry hpc automated addition for phagefactor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phagefactor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phagefactor:1.2.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phagefactor/1.2.0--hdfd78af_0
$ module help quay.io/biocontainers/phagefactor/1.2.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phagefactor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phagefactor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phagefactor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phagefactor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phagefactor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phagefactor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### create_custom_hmm.py

```bash
$ singularity exec <container> /usr/local/bin/create_custom_hmm.py
$ podman run --it --rm --entrypoint /usr/local/bin/create_custom_hmm.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_custom_hmm.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnaapler

```bash
$ singularity exec <container> /usr/local/bin/dnaapler
$ podman run --it --rm --entrypoint /usr/local/bin/dnaapler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnaapler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genbank.py

```bash
$ singularity exec <container> /usr/local/bin/genbank.py
$ podman run --it --rm --entrypoint /usr/local/bin/genbank.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genbank.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate-slurm-partition-config

```bash
$ singularity exec <container> /usr/local/bin/generate-slurm-partition-config
$ podman run --it --rm --entrypoint /usr/local/bin/generate-slurm-partition-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate-slurm-partition-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### install_databases.py

```bash
$ singularity exec <container> /usr/local/bin/install_databases.py
$ podman run --it --rm --entrypoint /usr/local/bin/install_databases.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/install_databases.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phagefactor

```bash
$ singularity exec <container> /usr/local/bin/phagefactor
$ podman run --it --rm --entrypoint /usr/local/bin/phagefactor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phagefactor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phanotate.py

```bash
$ singularity exec <container> /usr/local/bin/phanotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/phanotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phanotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pharokka

```bash
$ singularity exec <container> /usr/local/bin/pharokka
$ podman run --it --rm --entrypoint /usr/local/bin/pharokka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pharokka   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pharokka.py

```bash
$ singularity exec <container> /usr/local/bin/pharokka.py
$ podman run --it --rm --entrypoint /usr/local/bin/pharokka.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pharokka.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pharokka_multiplotter.py

```bash
$ singularity exec <container> /usr/local/bin/pharokka_multiplotter.py
$ podman run --it --rm --entrypoint /usr/local/bin/pharokka_multiplotter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pharokka_multiplotter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pharokka_plotter.py

```bash
$ singularity exec <container> /usr/local/bin/pharokka_plotter.py
$ podman run --it --rm --entrypoint /usr/local/bin/pharokka_plotter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pharokka_plotter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pharokka_proteins.py

```bash
$ singularity exec <container> /usr/local/bin/pharokka_proteins.py
$ podman run --it --rm --entrypoint /usr/local/bin/pharokka_proteins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pharokka_proteins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phold

```bash
$ singularity exec <container> /usr/local/bin/phold
$ podman run --it --rm --entrypoint /usr/local/bin/phold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrodigal-rv

```bash
$ singularity exec <container> /usr/local/bin/pyrodigal-rv
$ podman run --it --rm --entrypoint /usr/local/bin/pyrodigal-rv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrodigal-rv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spm_decode

```bash
$ singularity exec <container> /usr/local/bin/spm_decode
$ podman run --it --rm --entrypoint /usr/local/bin/spm_decode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spm_decode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spm_encode

```bash
$ singularity exec <container> /usr/local/bin/spm_encode
$ podman run --it --rm --entrypoint /usr/local/bin/spm_encode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spm_encode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spm_export_vocab

```bash
$ singularity exec <container> /usr/local/bin/spm_export_vocab
$ podman run --it --rm --entrypoint /usr/local/bin/spm_export_vocab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spm_export_vocab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spm_normalize

```bash
$ singularity exec <container> /usr/local/bin/spm_normalize
$ podman run --it --rm --entrypoint /usr/local/bin/spm_normalize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spm_normalize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spm_train

```bash
$ singularity exec <container> /usr/local/bin/spm_train
$ podman run --it --rm --entrypoint /usr/local/bin/spm_train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spm_train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### foldseek

```bash
$ singularity exec <container> /usr/local/bin/foldseek
$ podman run --it --rm --entrypoint /usr/local/bin/foldseek   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/foldseek   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MitoHighConfidenceFilter

```bash
$ singularity exec <container> /usr/local/bin/MitoHighConfidenceFilter
$ podman run --it --rm --entrypoint /usr/local/bin/MitoHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MitoHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### datasets-cli

```bash
$ singularity exec <container> /usr/local/bin/datasets-cli
$ podman run --it --rm --entrypoint /usr/local/bin/datasets-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datasets-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrodigal-gv

```bash
$ singularity exec <container> /usr/local/bin/pyrodigal-gv
$ podman run --it --rm --entrypoint /usr/local/bin/pyrodigal-gv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrodigal-gv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transformers

```bash
$ singularity exec <container> /usr/local/bin/transformers
$ podman run --it --rm --entrypoint /usr/local/bin/transformers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transformers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### black

```bash
$ singularity exec <container> /usr/local/bin/black
$ podman run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blackd

```bash
$ singularity exec <container> /usr/local/bin/blackd
$ podman run --it --rm --entrypoint /usr/local/bin/blackd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blackd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isort-identify-imports

```bash
$ singularity exec <container> /usr/local/bin/isort-identify-imports
$ podman run --it --rm --entrypoint /usr/local/bin/isort-identify-imports   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isort-identify-imports   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isort

```bash
$ singularity exec <container> /usr/local/bin/isort
$ podman run --it --rm --entrypoint /usr/local/bin/isort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.4.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.4.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EukHighConfidenceFilter

```bash
$ singularity exec <container> /usr/local/bin/EukHighConfidenceFilter
$ podman run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### covels-SE

```bash
$ singularity exec <container> /usr/local/bin/covels-SE
$ podman run --it --rm --entrypoint /usr/local/bin/covels-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/covels-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coves-SE

```bash
$ singularity exec <container> /usr/local/bin/coves-SE
$ podman run --it --rm --entrypoint /usr/local/bin/coves-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coves-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eufindtRNA

```bash
$ singularity exec <container> /usr/local/bin/eufindtRNA
$ podman run --it --rm --entrypoint /usr/local/bin/eufindtRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eufindtRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2gsi

```bash
$ singularity exec <container> /usr/local/bin/fasta2gsi
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2gsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2gsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hf

```bash
$ singularity exec <container> /usr/local/bin/hf
$ podman run --it --rm --entrypoint /usr/local/bin/hf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-28.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-28.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-28.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-28.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sstofa

```bash
$ singularity exec <container> /usr/local/bin/sstofa
$ podman run --it --rm --entrypoint /usr/local/bin/sstofa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sstofa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tRNAscan-SE

```bash
$ singularity exec <container> /usr/local/bin/tRNAscan-SE
$ podman run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tRNAscan-SE.conf

```bash
$ singularity exec <container> /usr/local/bin/tRNAscan-SE.conf
$ podman run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trnascan-1.4

```bash
$ singularity exec <container> /usr/local/bin/trnascan-1.4
$ podman run --it --rm --entrypoint /usr/local/bin/trnascan-1.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trnascan-1.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage

```bash
$ singularity exec <container> /usr/local/bin/coverage
$ podman run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiny-agents

```bash
$ singularity exec <container> /usr/local/bin/tiny-agents
$ podman run --it --rm --entrypoint /usr/local/bin/tiny-agents   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiny-agents   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### huggingface-cli

```bash
$ singularity exec <container> /usr/local/bin/huggingface-cli
$ podman run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minced

```bash
$ singularity exec <container> /usr/local/bin/minced
$ podman run --it --rm --entrypoint /usr/local/bin/minced   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minced   -v ${PWD} -w ${PWD} <container> -c " $@"
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