---
layout: container
name:  "quay.io/biocontainers/sar11-genome-atlas-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sar11-genome-atlas-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sar11-genome-atlas-tools/container.yaml"
updated_at: "2026-08-25 09:56:11.395810"
latest: "0.1.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/sar11-genome-atlas-tools"
aliases:
 - "epa-ng"
 - "gawk-5.4.1"
 - "sga-classify"
 - "sga-db"
 - "sga-map"
 - "sga-mapper"
 - "sga-run"
 - "fastANI"
 - "gawkbug"
 - "prodigal"
 - "mafft-sparsecore.rb"
 - "einsi"
 - "fftns"
 - "fftnsi"
 - "ginsi"
 - "linsi"
 - "mafft-distance"
 - "mafft-einsi"
 - "mafft-fftns"
 - "mafft-fftnsi"
 - "mafft-ginsi"
 - "mafft-homologs.rb"
 - "mafft-linsi"
 - "mafft-nwns"
 - "mafft-nwnsi"
 - "mafft-profile"
 - "mafft-qinsi"
 - "mafft-xinsi"
 - "nwns"
 - "nwnsi"
 - "mafft"
 - "gawk"
versions:
 - "0.1.8--pyhdfd78af_0"
description: "singularity registry hpc automated addition for sar11-genome-atlas-tools"
config: {"url": "https://biocontainers.pro/tools/sar11-genome-atlas-tools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sar11-genome-atlas-tools", "latest": {"0.1.8--pyhdfd78af_0": "sha256:b06b64cf41af714e2399a52c0486c01f11be8e318fec9ab4cc8bcee4b02d6a58"}, "tags": {"0.1.8--pyhdfd78af_0": "sha256:b06b64cf41af714e2399a52c0486c01f11be8e318fec9ab4cc8bcee4b02d6a58"}, "docker": "quay.io/biocontainers/sar11-genome-atlas-tools", "aliases": {"epa-ng": "/usr/local/bin/epa-ng", "gawk-5.4.1": "/usr/local/bin/gawk-5.4.1", "sga-classify": "/usr/local/bin/sga-classify", "sga-db": "/usr/local/bin/sga-db", "sga-map": "/usr/local/bin/sga-map", "sga-mapper": "/usr/local/bin/sga-mapper", "sga-run": "/usr/local/bin/sga-run", "fastANI": "/usr/local/bin/fastANI", "gawkbug": "/usr/local/bin/gawkbug", "prodigal": "/usr/local/bin/prodigal", "mafft-sparsecore.rb": "/usr/local/bin/mafft-sparsecore.rb", "einsi": "/usr/local/bin/einsi", "fftns": "/usr/local/bin/fftns", "fftnsi": "/usr/local/bin/fftnsi", "ginsi": "/usr/local/bin/ginsi", "linsi": "/usr/local/bin/linsi", "mafft-distance": "/usr/local/bin/mafft-distance", "mafft-einsi": "/usr/local/bin/mafft-einsi", "mafft-fftns": "/usr/local/bin/mafft-fftns", "mafft-fftnsi": "/usr/local/bin/mafft-fftnsi", "mafft-ginsi": "/usr/local/bin/mafft-ginsi", "mafft-homologs.rb": "/usr/local/bin/mafft-homologs.rb", "mafft-linsi": "/usr/local/bin/mafft-linsi", "mafft-nwns": "/usr/local/bin/mafft-nwns", "mafft-nwnsi": "/usr/local/bin/mafft-nwnsi", "mafft-profile": "/usr/local/bin/mafft-profile", "mafft-qinsi": "/usr/local/bin/mafft-qinsi", "mafft-xinsi": "/usr/local/bin/mafft-xinsi", "nwns": "/usr/local/bin/nwns", "nwnsi": "/usr/local/bin/nwnsi", "mafft": "/usr/local/bin/mafft", "gawk": "/usr/local/bin/gawk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sar11-genome-atlas-tools.
singularity registry hpc automated addition for sar11-genome-atlas-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sar11-genome-atlas-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sar11-genome-atlas-tools:0.1.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sar11-genome-atlas-tools/0.1.8--pyhdfd78af_0
$ module help quay.io/biocontainers/sar11-genome-atlas-tools/0.1.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sar11-genome-atlas-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sar11-genome-atlas-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sar11-genome-atlas-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sar11-genome-atlas-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sar11-genome-atlas-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sar11-genome-atlas-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### epa-ng

```bash
$ singularity exec <container> /usr/local/bin/epa-ng
$ podman run --it --rm --entrypoint /usr/local/bin/epa-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epa-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.4.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.4.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sga-classify

```bash
$ singularity exec <container> /usr/local/bin/sga-classify
$ podman run --it --rm --entrypoint /usr/local/bin/sga-classify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sga-classify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sga-db

```bash
$ singularity exec <container> /usr/local/bin/sga-db
$ podman run --it --rm --entrypoint /usr/local/bin/sga-db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sga-db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sga-map

```bash
$ singularity exec <container> /usr/local/bin/sga-map
$ podman run --it --rm --entrypoint /usr/local/bin/sga-map   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sga-map   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sga-mapper

```bash
$ singularity exec <container> /usr/local/bin/sga-mapper
$ podman run --it --rm --entrypoint /usr/local/bin/sga-mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sga-mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sga-run

```bash
$ singularity exec <container> /usr/local/bin/sga-run
$ podman run --it --rm --entrypoint /usr/local/bin/sga-run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sga-run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastANI

```bash
$ singularity exec <container> /usr/local/bin/fastANI
$ podman run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prodigal

```bash
$ singularity exec <container> /usr/local/bin/prodigal
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mafft-fftns

```bash
$ singularity exec <container> /usr/local/bin/mafft-fftns
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-fftnsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-fftnsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-ginsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-ginsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-homologs.rb

```bash
$ singularity exec <container> /usr/local/bin/mafft-homologs.rb
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-homologs.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-homologs.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-linsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-linsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-nwns

```bash
$ singularity exec <container> /usr/local/bin/mafft-nwns
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-nwns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-nwns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-nwnsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-nwnsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-nwnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-nwnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-profile

```bash
$ singularity exec <container> /usr/local/bin/mafft-profile
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-qinsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-qinsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-qinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-qinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-xinsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-xinsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-xinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-xinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nwns

```bash
$ singularity exec <container> /usr/local/bin/nwns
$ podman run --it --rm --entrypoint /usr/local/bin/nwns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nwns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nwnsi

```bash
$ singularity exec <container> /usr/local/bin/nwnsi
$ podman run --it --rm --entrypoint /usr/local/bin/nwnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nwnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft

```bash
$ singularity exec <container> /usr/local/bin/mafft
$ podman run --it --rm --entrypoint /usr/local/bin/mafft   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
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