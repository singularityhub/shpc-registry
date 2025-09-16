---
layout: container
name:  "quay.io/biocontainers/magus-msa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/magus-msa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/magus-msa/container.yaml"
updated_at: "2025-09-16 04:04:59.015309"
latest: "0.2.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/magus-msa"
aliases:
 - "blastn_vdb"
 - "magus"
 - "rcl"
 - "rcl-dot-resmap.pl"
 - "rcl-qc"
 - "rcl-qm.R"
 - "rcl-relevel.pl"
 - "rcl-select.pl"
 - "rcldo.pl"
 - "tblastn_vdb"
 - "clustalo"
 - "uuid"
 - "uuid-config"
 - "clm"
 - "clxdo"
 - "mcl"
 - "mcx"
 - "mcxarray"
 - "mcxdump"
 - "mcxi"
 - "mcxload"
 - "mcxmap"
 - "mcxsubs"
 - "dendropy-format"
 - "test_pcre"
 - "FastTreeMP"
 - "FastTree"
 - "sumlabels.py"
 - "fasttree"
 - "sumtrees.py"
 - "mafft-sparsecore.rb"
 - "einsi"
 - "fftns"
 - "fftnsi"
 - "ginsi"
versions:
 - "0.1.2--pyhdfd78af_0"
 - "0.1.3--pyhdfd78af_0"
 - "0.2.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for magus-msa"
config: {"url": "https://biocontainers.pro/tools/magus-msa", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for magus-msa", "latest": {"0.2.0--pyhdfd78af_0": "sha256:5b3c332fd718f82ecadb8a2bc3b1fd6abd9d87e42946f193277f4437ce1aec9c"}, "tags": {"0.1.2--pyhdfd78af_0": "sha256:cd01e1b765c786ffcbb47651a2bd0146e6f1e69a992ee09c6ae7e8b5847bed5a", "0.1.3--pyhdfd78af_0": "sha256:059079a6be8fe5a175a0069ef15b989bac53223fac550791cc03dca976b474db", "0.2.0--pyhdfd78af_0": "sha256:5b3c332fd718f82ecadb8a2bc3b1fd6abd9d87e42946f193277f4437ce1aec9c"}, "docker": "quay.io/biocontainers/magus-msa", "aliases": {"blastn_vdb": "/usr/local/bin/blastn_vdb", "magus": "/usr/local/bin/magus", "rcl": "/usr/local/bin/rcl", "rcl-dot-resmap.pl": "/usr/local/bin/rcl-dot-resmap.pl", "rcl-qc": "/usr/local/bin/rcl-qc", "rcl-qm.R": "/usr/local/bin/rcl-qm.R", "rcl-relevel.pl": "/usr/local/bin/rcl-relevel.pl", "rcl-select.pl": "/usr/local/bin/rcl-select.pl", "rcldo.pl": "/usr/local/bin/rcldo.pl", "tblastn_vdb": "/usr/local/bin/tblastn_vdb", "clustalo": "/usr/local/bin/clustalo", "uuid": "/usr/local/bin/uuid", "uuid-config": "/usr/local/bin/uuid-config", "clm": "/usr/local/bin/clm", "clxdo": "/usr/local/bin/clxdo", "mcl": "/usr/local/bin/mcl", "mcx": "/usr/local/bin/mcx", "mcxarray": "/usr/local/bin/mcxarray", "mcxdump": "/usr/local/bin/mcxdump", "mcxi": "/usr/local/bin/mcxi", "mcxload": "/usr/local/bin/mcxload", "mcxmap": "/usr/local/bin/mcxmap", "mcxsubs": "/usr/local/bin/mcxsubs", "dendropy-format": "/usr/local/bin/dendropy-format", "test_pcre": "/usr/local/bin/test_pcre", "FastTreeMP": "/usr/local/bin/FastTreeMP", "FastTree": "/usr/local/bin/FastTree", "sumlabels.py": "/usr/local/bin/sumlabels.py", "fasttree": "/usr/local/bin/fasttree", "sumtrees.py": "/usr/local/bin/sumtrees.py", "mafft-sparsecore.rb": "/usr/local/bin/mafft-sparsecore.rb", "einsi": "/usr/local/bin/einsi", "fftns": "/usr/local/bin/fftns", "fftnsi": "/usr/local/bin/fftnsi", "ginsi": "/usr/local/bin/ginsi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/magus-msa.
singularity registry hpc automated addition for magus-msa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/magus-msa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/magus-msa:0.2.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/magus-msa/0.2.0--pyhdfd78af_0
$ module help quay.io/biocontainers/magus-msa/0.2.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### magus-msa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### magus-msa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### magus-msa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### magus-msa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### magus-msa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### magus-msa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### blastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/blastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magus

```bash
$ singularity exec <container> /usr/local/bin/magus
$ podman run --it --rm --entrypoint /usr/local/bin/magus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rcl

```bash
$ singularity exec <container> /usr/local/bin/rcl
$ podman run --it --rm --entrypoint /usr/local/bin/rcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rcl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rcl-dot-resmap.pl

```bash
$ singularity exec <container> /usr/local/bin/rcl-dot-resmap.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rcl-dot-resmap.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rcl-dot-resmap.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rcl-qc

```bash
$ singularity exec <container> /usr/local/bin/rcl-qc
$ podman run --it --rm --entrypoint /usr/local/bin/rcl-qc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rcl-qc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rcl-qm.R

```bash
$ singularity exec <container> /usr/local/bin/rcl-qm.R
$ podman run --it --rm --entrypoint /usr/local/bin/rcl-qm.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rcl-qm.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rcl-relevel.pl

```bash
$ singularity exec <container> /usr/local/bin/rcl-relevel.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rcl-relevel.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rcl-relevel.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rcl-select.pl

```bash
$ singularity exec <container> /usr/local/bin/rcl-select.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rcl-select.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rcl-select.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rcldo.pl

```bash
$ singularity exec <container> /usr/local/bin/rcldo.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rcldo.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rcldo.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tblastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/tblastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalo

```bash
$ singularity exec <container> /usr/local/bin/clustalo
$ podman run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uuid

```bash
$ singularity exec <container> /usr/local/bin/uuid
$ podman run --it --rm --entrypoint /usr/local/bin/uuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uuid-config

```bash
$ singularity exec <container> /usr/local/bin/uuid-config
$ podman run --it --rm --entrypoint /usr/local/bin/uuid-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uuid-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clm

```bash
$ singularity exec <container> /usr/local/bin/clm
$ podman run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clxdo

```bash
$ singularity exec <container> /usr/local/bin/clxdo
$ podman run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcl

```bash
$ singularity exec <container> /usr/local/bin/mcl
$ podman run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcx

```bash
$ singularity exec <container> /usr/local/bin/mcx
$ podman run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxarray

```bash
$ singularity exec <container> /usr/local/bin/mcxarray
$ podman run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxdump

```bash
$ singularity exec <container> /usr/local/bin/mcxdump
$ podman run --it --rm --entrypoint /usr/local/bin/mcxdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxi

```bash
$ singularity exec <container> /usr/local/bin/mcxi
$ podman run --it --rm --entrypoint /usr/local/bin/mcxi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxload

```bash
$ singularity exec <container> /usr/local/bin/mcxload
$ podman run --it --rm --entrypoint /usr/local/bin/mcxload   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxload   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxmap

```bash
$ singularity exec <container> /usr/local/bin/mcxmap
$ podman run --it --rm --entrypoint /usr/local/bin/mcxmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxsubs

```bash
$ singularity exec <container> /usr/local/bin/mcxsubs
$ podman run --it --rm --entrypoint /usr/local/bin/mcxsubs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxsubs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_pcre

```bash
$ singularity exec <container> /usr/local/bin/test_pcre
$ podman run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTreeMP

```bash
$ singularity exec <container> /usr/local/bin/FastTreeMP
$ podman run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree

```bash
$ singularity exec <container> /usr/local/bin/FastTree
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumlabels.py

```bash
$ singularity exec <container> /usr/local/bin/sumlabels.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasttree

```bash
$ singularity exec <container> /usr/local/bin/fasttree
$ podman run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumtrees.py

```bash
$ singularity exec <container> /usr/local/bin/sumtrees.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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