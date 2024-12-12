---
layout: container
name:  "quay.io/biocontainers/pyani"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyani/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyani/container.yaml"
updated_at: "2024-12-12 03:17:46.889649"
latest: "0.2.13.1--pyhdc42f0e_0"
container_url: "https://biocontainers.pro/tools/pyani"
aliases:
 - "average_nucleotide_identity.py"
 - "delta_filter_wrapper.py"
 - "genbank_get_genomes_by_taxon.py"
 - "bl2seq"
 - "blastall"
 - "blastclust"
 - "blastpgp"
 - "copymat"
 - "fastacmd"
 - "formatdb"
 - "formatrpsdb"
 - "impala"
 - "makemat"
versions:
 - "0.2.9--pyh24bf2e0_0"
 - "0.2.12--pyhdfd78af_0"
 - "0.2.13.1--pyhdc42f0e_0"
description: "shpc-registry automated BioContainers addition for pyani"
config: {"url": "https://biocontainers.pro/tools/pyani", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyani", "latest": {"0.2.13.1--pyhdc42f0e_0": "sha256:14af7779ad0fb70224a0a182be537f0ede440ce9424cb3456cbc85012bff2884"}, "tags": {"0.2.9--pyh24bf2e0_0": "sha256:e5e6fadb1c17bb832f8d3f32e24ef14f4891fff22128defca8eebe9357a5d4eb", "0.2.12--pyhdfd78af_0": "sha256:255c207f0fec533ce143de5c106e1f1a442c466a4b0179e324cedfdbae96394e", "0.2.13.1--pyhdc42f0e_0": "sha256:14af7779ad0fb70224a0a182be537f0ede440ce9424cb3456cbc85012bff2884"}, "docker": "quay.io/biocontainers/pyani", "aliases": {"average_nucleotide_identity.py": "/usr/local/bin/average_nucleotide_identity.py", "delta_filter_wrapper.py": "/usr/local/bin/delta_filter_wrapper.py", "genbank_get_genomes_by_taxon.py": "/usr/local/bin/genbank_get_genomes_by_taxon.py", "bl2seq": "/usr/local/bin/bl2seq", "blastall": "/usr/local/bin/blastall", "blastclust": "/usr/local/bin/blastclust", "blastpgp": "/usr/local/bin/blastpgp", "copymat": "/usr/local/bin/copymat", "fastacmd": "/usr/local/bin/fastacmd", "formatdb": "/usr/local/bin/formatdb", "formatrpsdb": "/usr/local/bin/formatrpsdb", "impala": "/usr/local/bin/impala", "makemat": "/usr/local/bin/makemat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyani.
shpc-registry automated BioContainers addition for pyani
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyani
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyani:0.2.13.1--pyhdc42f0e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyani/0.2.13.1--pyhdc42f0e_0
$ module help quay.io/biocontainers/pyani/0.2.13.1--pyhdc42f0e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyani-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyani-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyani-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyani-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyani-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyani-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### average_nucleotide_identity.py

```bash
$ singularity exec <container> /usr/local/bin/average_nucleotide_identity.py
$ podman run --it --rm --entrypoint /usr/local/bin/average_nucleotide_identity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/average_nucleotide_identity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta_filter_wrapper.py

```bash
$ singularity exec <container> /usr/local/bin/delta_filter_wrapper.py
$ podman run --it --rm --entrypoint /usr/local/bin/delta_filter_wrapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta_filter_wrapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genbank_get_genomes_by_taxon.py

```bash
$ singularity exec <container> /usr/local/bin/genbank_get_genomes_by_taxon.py
$ podman run --it --rm --entrypoint /usr/local/bin/genbank_get_genomes_by_taxon.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genbank_get_genomes_by_taxon.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl2seq

```bash
$ singularity exec <container> /usr/local/bin/bl2seq
$ podman run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastall

```bash
$ singularity exec <container> /usr/local/bin/blastall
$ podman run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastclust

```bash
$ singularity exec <container> /usr/local/bin/blastclust
$ podman run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastpgp

```bash
$ singularity exec <container> /usr/local/bin/blastpgp
$ podman run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### copymat

```bash
$ singularity exec <container> /usr/local/bin/copymat
$ podman run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastacmd

```bash
$ singularity exec <container> /usr/local/bin/fastacmd
$ podman run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatdb

```bash
$ singularity exec <container> /usr/local/bin/formatdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatrpsdb

```bash
$ singularity exec <container> /usr/local/bin/formatrpsdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### impala

```bash
$ singularity exec <container> /usr/local/bin/impala
$ podman run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makemat

```bash
$ singularity exec <container> /usr/local/bin/makemat
$ podman run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
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