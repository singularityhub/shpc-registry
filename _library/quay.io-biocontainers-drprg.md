---
layout: container
name:  "quay.io/biocontainers/drprg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/drprg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/drprg/container.yaml"
updated_at: "2024-10-17 03:13:56.283316"
latest: "0.1.1--h5076881_1"
container_url: "https://biocontainers.pro/tools/drprg"
aliases:
 - "drprg"
 - "make_prg"
 - "pandora"
 - "gff2gff.py"
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
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
versions:
 - "0.1.1--h1f4ba0c_0"
 - "0.1.1--h5076881_1"
description: "singularity registry hpc automated addition for drprg"
config: {"url": "https://biocontainers.pro/tools/drprg", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for drprg", "latest": {"0.1.1--h5076881_1": "sha256:908e10aa922f4baea18cc31ef4879e552bbdaacf8266833b8e175e4e766363e1"}, "tags": {"0.1.1--h1f4ba0c_0": "sha256:78e5ae97a6661f5da1eb61090518f8fc01455f91b3541e8fd0d856e29d74f950", "0.1.1--h5076881_1": "sha256:908e10aa922f4baea18cc31ef4879e552bbdaacf8266833b8e175e4e766363e1"}, "docker": "quay.io/biocontainers/drprg", "aliases": {"drprg": "/usr/local/bin/drprg", "make_prg": "/usr/local/bin/make_prg", "pandora": "/usr/local/bin/pandora", "gff2gff.py": "/usr/local/bin/gff2gff.py", "mafft-sparsecore.rb": "/usr/local/bin/mafft-sparsecore.rb", "einsi": "/usr/local/bin/einsi", "fftns": "/usr/local/bin/fftns", "fftnsi": "/usr/local/bin/fftnsi", "ginsi": "/usr/local/bin/ginsi", "linsi": "/usr/local/bin/linsi", "mafft-distance": "/usr/local/bin/mafft-distance", "mafft-einsi": "/usr/local/bin/mafft-einsi", "mafft-fftns": "/usr/local/bin/mafft-fftns", "mafft-fftnsi": "/usr/local/bin/mafft-fftnsi", "mafft-ginsi": "/usr/local/bin/mafft-ginsi", "mafft-homologs.rb": "/usr/local/bin/mafft-homologs.rb", "mafft-linsi": "/usr/local/bin/mafft-linsi", "mafft-nwns": "/usr/local/bin/mafft-nwns", "mafft-nwnsi": "/usr/local/bin/mafft-nwnsi", "mafft-profile": "/usr/local/bin/mafft-profile", "mafft-qinsi": "/usr/local/bin/mafft-qinsi", "mafft-xinsi": "/usr/local/bin/mafft-xinsi", "nwns": "/usr/local/bin/nwns", "nwnsi": "/usr/local/bin/nwnsi", "mafft": "/usr/local/bin/mafft", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/drprg.
singularity registry hpc automated addition for drprg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/drprg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/drprg:0.1.1--h5076881_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/drprg/0.1.1--h5076881_1
$ module help quay.io/biocontainers/drprg/0.1.1--h5076881_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### drprg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### drprg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### drprg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### drprg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### drprg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### drprg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### drprg

```bash
$ singularity exec <container> /usr/local/bin/drprg
$ podman run --it --rm --entrypoint /usr/local/bin/drprg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/drprg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_prg

```bash
$ singularity exec <container> /usr/local/bin/make_prg
$ podman run --it --rm --entrypoint /usr/local/bin/make_prg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_prg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandora

```bash
$ singularity exec <container> /usr/local/bin/pandora
$ podman run --it --rm --entrypoint /usr/local/bin/pandora   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandora   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-roh.py

```bash
$ singularity exec <container> /usr/local/bin/plot-roh.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-roh.pl

```bash
$ singularity exec <container> /usr/local/bin/run-roh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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