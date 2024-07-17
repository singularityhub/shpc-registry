---
layout: container
name:  "quay.io/biocontainers/mitos"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mitos/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mitos/container.yaml"
updated_at: "2024-07-17 02:47:23.126004"
latest: "2.1.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mitos"
aliases:
 - "analyse.py"
 - "gcpp.py"
 - "geneorder.py"
 - "getfeatures.py"
 - "getinfo.py"
 - "plotprot.R"
 - "plotrna.R"
 - "plotstst.R"
 - "refseqsplit.py"
 - "runmitos.py"
 - "subseq.py"
 - "taxtree.py"
 - "update-blastdb.py"
 - "RNAfold"
 - "Kinfold"
 - "RNALfold"
 - "RNAaliduplex"
 - "RNAalifold"
 - "RNAcofold"
 - "RNAdistance"
 - "RNAduplex"
 - "RNAeval"
 - "RNAforester"
versions:
 - "2.1.0--pyhdfd78af_0"
 - "2.1.3--pyhdfd78af_0"
 - "2.1.6--pyhdfd78af_1"
 - "2.1.7--pyhdfd78af_0"
 - "2.1.7--pyhdfd78af_1"
 - "2.1.8--pyhdfd78af_0"
 - "2.1.9--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for mitos"
config: {"url": "https://biocontainers.pro/tools/mitos", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mitos", "latest": {"2.1.9--pyhdfd78af_0": "sha256:b4fd792cee016fdadfac7a1d51de10fd957c2e17e939dd8e262d835fb0fbc25f"}, "tags": {"2.1.0--pyhdfd78af_0": "sha256:5a17df47ea636c4fd46f2b7cd173e8551446228b4baca21dc20392b1d43503d9", "2.1.3--pyhdfd78af_0": "sha256:3b596a3d0cbb57946e1d0aa886cf9b38e52c422f8fc4e4e6d767e101baeb1483", "2.1.6--pyhdfd78af_1": "sha256:f19404b86e0448e39d2a672f1d89c7f2d2e2fbf4a2c75ebb146e11f92ba233b2", "2.1.7--pyhdfd78af_0": "sha256:2bde03061de290547f6886db226cd947fab73403ff3414647fba483d4b64b497", "2.1.7--pyhdfd78af_1": "sha256:2447475c09bf7637a74f63037d833039ba1c6387ecfdff606e367310a03b1224", "2.1.8--pyhdfd78af_0": "sha256:99060b9d898d62f3d0e32cdb8bd39edff496d7f27f2c02a705527adc3c46ff4f", "2.1.9--pyhdfd78af_0": "sha256:b4fd792cee016fdadfac7a1d51de10fd957c2e17e939dd8e262d835fb0fbc25f"}, "docker": "quay.io/biocontainers/mitos", "aliases": {"analyse.py": "/usr/local/bin/analyse.py", "gcpp.py": "/usr/local/bin/gcpp.py", "geneorder.py": "/usr/local/bin/geneorder.py", "getfeatures.py": "/usr/local/bin/getfeatures.py", "getinfo.py": "/usr/local/bin/getinfo.py", "plotprot.R": "/usr/local/bin/plotprot.R", "plotrna.R": "/usr/local/bin/plotrna.R", "plotstst.R": "/usr/local/bin/plotstst.R", "refseqsplit.py": "/usr/local/bin/refseqsplit.py", "runmitos.py": "/usr/local/bin/runmitos.py", "subseq.py": "/usr/local/bin/subseq.py", "taxtree.py": "/usr/local/bin/taxtree.py", "update-blastdb.py": "/usr/local/bin/update-blastdb.py", "RNAfold": "/usr/local/bin/RNAfold", "Kinfold": "/usr/local/bin/Kinfold", "RNALfold": "/usr/local/bin/RNALfold", "RNAaliduplex": "/usr/local/bin/RNAaliduplex", "RNAalifold": "/usr/local/bin/RNAalifold", "RNAcofold": "/usr/local/bin/RNAcofold", "RNAdistance": "/usr/local/bin/RNAdistance", "RNAduplex": "/usr/local/bin/RNAduplex", "RNAeval": "/usr/local/bin/RNAeval", "RNAforester": "/usr/local/bin/RNAforester"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mitos.
shpc-registry automated BioContainers addition for mitos
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mitos
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mitos:2.1.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mitos/2.1.9--pyhdfd78af_0
$ module help quay.io/biocontainers/mitos/2.1.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mitos-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mitos-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mitos-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mitos-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mitos-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mitos-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### analyse.py

```bash
$ singularity exec <container> /usr/local/bin/analyse.py
$ podman run --it --rm --entrypoint /usr/local/bin/analyse.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyse.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcpp.py

```bash
$ singularity exec <container> /usr/local/bin/gcpp.py
$ podman run --it --rm --entrypoint /usr/local/bin/gcpp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcpp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geneorder.py

```bash
$ singularity exec <container> /usr/local/bin/geneorder.py
$ podman run --it --rm --entrypoint /usr/local/bin/geneorder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geneorder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getfeatures.py

```bash
$ singularity exec <container> /usr/local/bin/getfeatures.py
$ podman run --it --rm --entrypoint /usr/local/bin/getfeatures.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getfeatures.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getinfo.py

```bash
$ singularity exec <container> /usr/local/bin/getinfo.py
$ podman run --it --rm --entrypoint /usr/local/bin/getinfo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getinfo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotprot.R

```bash
$ singularity exec <container> /usr/local/bin/plotprot.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotprot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotprot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotrna.R

```bash
$ singularity exec <container> /usr/local/bin/plotrna.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotrna.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotrna.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotstst.R

```bash
$ singularity exec <container> /usr/local/bin/plotstst.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotstst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotstst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refseqsplit.py

```bash
$ singularity exec <container> /usr/local/bin/refseqsplit.py
$ podman run --it --rm --entrypoint /usr/local/bin/refseqsplit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refseqsplit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runmitos.py

```bash
$ singularity exec <container> /usr/local/bin/runmitos.py
$ podman run --it --rm --entrypoint /usr/local/bin/runmitos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runmitos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subseq.py

```bash
$ singularity exec <container> /usr/local/bin/subseq.py
$ podman run --it --rm --entrypoint /usr/local/bin/subseq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subseq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxtree.py

```bash
$ singularity exec <container> /usr/local/bin/taxtree.py
$ podman run --it --rm --entrypoint /usr/local/bin/taxtree.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxtree.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update-blastdb.py

```bash
$ singularity exec <container> /usr/local/bin/update-blastdb.py
$ podman run --it --rm --entrypoint /usr/local/bin/update-blastdb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update-blastdb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAfold

```bash
$ singularity exec <container> /usr/local/bin/RNAfold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Kinfold

```bash
$ singularity exec <container> /usr/local/bin/Kinfold
$ podman run --it --rm --entrypoint /usr/local/bin/Kinfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Kinfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNALfold

```bash
$ singularity exec <container> /usr/local/bin/RNALfold
$ podman run --it --rm --entrypoint /usr/local/bin/RNALfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNALfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAaliduplex

```bash
$ singularity exec <container> /usr/local/bin/RNAaliduplex
$ podman run --it --rm --entrypoint /usr/local/bin/RNAaliduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAaliduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAalifold

```bash
$ singularity exec <container> /usr/local/bin/RNAalifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAcofold

```bash
$ singularity exec <container> /usr/local/bin/RNAcofold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAcofold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAcofold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAdistance

```bash
$ singularity exec <container> /usr/local/bin/RNAdistance
$ podman run --it --rm --entrypoint /usr/local/bin/RNAdistance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAdistance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAduplex

```bash
$ singularity exec <container> /usr/local/bin/RNAduplex
$ podman run --it --rm --entrypoint /usr/local/bin/RNAduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAeval

```bash
$ singularity exec <container> /usr/local/bin/RNAeval
$ podman run --it --rm --entrypoint /usr/local/bin/RNAeval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAeval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAforester

```bash
$ singularity exec <container> /usr/local/bin/RNAforester
$ podman run --it --rm --entrypoint /usr/local/bin/RNAforester   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAforester   -v ${PWD} -w ${PWD} <container> -c " $@"
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