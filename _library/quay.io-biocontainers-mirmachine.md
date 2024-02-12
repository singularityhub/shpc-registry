---
layout: container
name:  "quay.io/biocontainers/mirmachine"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mirmachine/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mirmachine/container.yaml"
updated_at: "2024-02-12 03:03:01.943818"
latest: "0.2.12--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mirmachine"
aliases:
 - "MirMachine.py"
 - "chronic"
 - "combine"
 - "errno"
 - "gff_sort_and_compete.sh"
 - "ifdata"
 - "ifne"
 - "isutf8"
 - "lckdo"
 - "mirmachine-tree-parser.py"
 - "mispipe"
 - "pee"
 - "sponge"
 - "ts"
 - "vidir"
 - "vipe"
 - "zrun"
 - "plac_runner.py"
 - "yte"
 - "cmark"
 - "pulptest"
 - "cbc"
 - "clp"
 - "cmalign"
 - "cmbuild"
 - "cmcalibrate"
 - "cmconvert"
versions:
 - "0.2.11.2022--pyhdfd78af_0"
 - "0.2.12--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for mirmachine"
config: {"url": "https://biocontainers.pro/tools/mirmachine", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mirmachine", "latest": {"0.2.12--pyhdfd78af_0": "sha256:7ac836a6ace24a9699019f388aceda491319e7656c56f8bbe1b8b4a67919a370"}, "tags": {"0.2.11.2022--pyhdfd78af_0": "sha256:401cdcd5fbc7c0065a7e3b18749252bf033370089fead42299f68f8c520b2dc7", "0.2.12--pyhdfd78af_0": "sha256:7ac836a6ace24a9699019f388aceda491319e7656c56f8bbe1b8b4a67919a370"}, "docker": "quay.io/biocontainers/mirmachine", "aliases": {"MirMachine.py": "/usr/local/bin/MirMachine.py", "chronic": "/usr/local/bin/chronic", "combine": "/usr/local/bin/combine", "errno": "/usr/local/bin/errno", "gff_sort_and_compete.sh": "/usr/local/bin/gff_sort_and_compete.sh", "ifdata": "/usr/local/bin/ifdata", "ifne": "/usr/local/bin/ifne", "isutf8": "/usr/local/bin/isutf8", "lckdo": "/usr/local/bin/lckdo", "mirmachine-tree-parser.py": "/usr/local/bin/mirmachine-tree-parser.py", "mispipe": "/usr/local/bin/mispipe", "pee": "/usr/local/bin/pee", "sponge": "/usr/local/bin/sponge", "ts": "/usr/local/bin/ts", "vidir": "/usr/local/bin/vidir", "vipe": "/usr/local/bin/vipe", "zrun": "/usr/local/bin/zrun", "plac_runner.py": "/usr/local/bin/plac_runner.py", "yte": "/usr/local/bin/yte", "cmark": "/usr/local/bin/cmark", "pulptest": "/usr/local/bin/pulptest", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp", "cmalign": "/usr/local/bin/cmalign", "cmbuild": "/usr/local/bin/cmbuild", "cmcalibrate": "/usr/local/bin/cmcalibrate", "cmconvert": "/usr/local/bin/cmconvert"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mirmachine.
shpc-registry automated BioContainers addition for mirmachine
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mirmachine
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mirmachine:0.2.12--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mirmachine/0.2.12--pyhdfd78af_0
$ module help quay.io/biocontainers/mirmachine/0.2.12--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mirmachine-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mirmachine-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mirmachine-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mirmachine-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mirmachine-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mirmachine-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MirMachine.py

```bash
$ singularity exec <container> /usr/local/bin/MirMachine.py
$ podman run --it --rm --entrypoint /usr/local/bin/MirMachine.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MirMachine.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chronic

```bash
$ singularity exec <container> /usr/local/bin/chronic
$ podman run --it --rm --entrypoint /usr/local/bin/chronic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chronic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine

```bash
$ singularity exec <container> /usr/local/bin/combine
$ podman run --it --rm --entrypoint /usr/local/bin/combine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### errno

```bash
$ singularity exec <container> /usr/local/bin/errno
$ podman run --it --rm --entrypoint /usr/local/bin/errno   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/errno   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff_sort_and_compete.sh

```bash
$ singularity exec <container> /usr/local/bin/gff_sort_and_compete.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gff_sort_and_compete.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff_sort_and_compete.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ifdata

```bash
$ singularity exec <container> /usr/local/bin/ifdata
$ podman run --it --rm --entrypoint /usr/local/bin/ifdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ifdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ifne

```bash
$ singularity exec <container> /usr/local/bin/ifne
$ podman run --it --rm --entrypoint /usr/local/bin/ifne   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ifne   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isutf8

```bash
$ singularity exec <container> /usr/local/bin/isutf8
$ podman run --it --rm --entrypoint /usr/local/bin/isutf8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isutf8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lckdo

```bash
$ singularity exec <container> /usr/local/bin/lckdo
$ podman run --it --rm --entrypoint /usr/local/bin/lckdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lckdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirmachine-tree-parser.py

```bash
$ singularity exec <container> /usr/local/bin/mirmachine-tree-parser.py
$ podman run --it --rm --entrypoint /usr/local/bin/mirmachine-tree-parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirmachine-tree-parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mispipe

```bash
$ singularity exec <container> /usr/local/bin/mispipe
$ podman run --it --rm --entrypoint /usr/local/bin/mispipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mispipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pee

```bash
$ singularity exec <container> /usr/local/bin/pee
$ podman run --it --rm --entrypoint /usr/local/bin/pee   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pee   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sponge

```bash
$ singularity exec <container> /usr/local/bin/sponge
$ podman run --it --rm --entrypoint /usr/local/bin/sponge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sponge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ts

```bash
$ singularity exec <container> /usr/local/bin/ts
$ podman run --it --rm --entrypoint /usr/local/bin/ts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vidir

```bash
$ singularity exec <container> /usr/local/bin/vidir
$ podman run --it --rm --entrypoint /usr/local/bin/vidir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vidir   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vipe

```bash
$ singularity exec <container> /usr/local/bin/vipe
$ podman run --it --rm --entrypoint /usr/local/bin/vipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zrun

```bash
$ singularity exec <container> /usr/local/bin/zrun
$ podman run --it --rm --entrypoint /usr/local/bin/zrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plac_runner.py

```bash
$ singularity exec <container> /usr/local/bin/plac_runner.py
$ podman run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yte

```bash
$ singularity exec <container> /usr/local/bin/yte
$ podman run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmark

```bash
$ singularity exec <container> /usr/local/bin/cmark
$ podman run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbc

```bash
$ singularity exec <container> /usr/local/bin/cbc
$ podman run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clp

```bash
$ singularity exec <container> /usr/local/bin/clp
$ podman run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmalign

```bash
$ singularity exec <container> /usr/local/bin/cmalign
$ podman run --it --rm --entrypoint /usr/local/bin/cmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmbuild

```bash
$ singularity exec <container> /usr/local/bin/cmbuild
$ podman run --it --rm --entrypoint /usr/local/bin/cmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmcalibrate

```bash
$ singularity exec <container> /usr/local/bin/cmcalibrate
$ podman run --it --rm --entrypoint /usr/local/bin/cmcalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmcalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmconvert

```bash
$ singularity exec <container> /usr/local/bin/cmconvert
$ podman run --it --rm --entrypoint /usr/local/bin/cmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
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