---
layout: container
name:  "quay.io/biocontainers/ciri3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ciri3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ciri3/container.yaml"
updated_at: "2026-10-30 08:48:05.282418"
latest: "3.0.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/ciri3"
aliases:
 - "FDR.py"
 - "RNASeq-MATS.py"
 - "STAR-avx"
 - "STAR-avx2"
 - "STAR-plain"
 - "STAR-sse3"
 - "STAR-sse4.1"
 - "STAR-ssse3"
 - "STARlong-avx"
 - "STARlong-avx2"
 - "STARlong-plain"
 - "STARlong-sse3"
 - "STARlong-sse4.1"
 - "STARlong-ssse3"
 - "ciri3"
 - "gmake"
 - "inclusion_level.py"
 - "joinFiles.py"
 - "paste.py"
 - "rmats.py"
 - "STAR"
 - "STARlong"
 - "jnativescan"
 - "fc-genconf"
 - "jwebserver"
 - "ref-cache"
 - "jpackage"
 - "annot-tsv"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "cups-config"
 - "ippeveprinter"
 - "ipptool"
 - "x86_64-conda-linux-gnu.cfg"
 - "jfr"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
 - "jmod"
 - "jshell"
 - "aserver"
 - "jdeps"
versions:
 - "3.0.1--hdfd78af_0"
description: "singularity registry hpc automated addition for ciri3"
config: {"url": "https://biocontainers.pro/tools/ciri3", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ciri3", "latest": {"3.0.1--hdfd78af_0": "sha256:428868f056472eae1f6e9ba305ff47497f4a8556a98cf6a1e5400fa782569aec"}, "tags": {"3.0.1--hdfd78af_0": "sha256:428868f056472eae1f6e9ba305ff47497f4a8556a98cf6a1e5400fa782569aec"}, "docker": "quay.io/biocontainers/ciri3", "aliases": {"FDR.py": "/usr/local/bin/FDR.py", "RNASeq-MATS.py": "/usr/local/bin/RNASeq-MATS.py", "STAR-avx": "/usr/local/bin/STAR-avx", "STAR-avx2": "/usr/local/bin/STAR-avx2", "STAR-plain": "/usr/local/bin/STAR-plain", "STAR-sse3": "/usr/local/bin/STAR-sse3", "STAR-sse4.1": "/usr/local/bin/STAR-sse4.1", "STAR-ssse3": "/usr/local/bin/STAR-ssse3", "STARlong-avx": "/usr/local/bin/STARlong-avx", "STARlong-avx2": "/usr/local/bin/STARlong-avx2", "STARlong-plain": "/usr/local/bin/STARlong-plain", "STARlong-sse3": "/usr/local/bin/STARlong-sse3", "STARlong-sse4.1": "/usr/local/bin/STARlong-sse4.1", "STARlong-ssse3": "/usr/local/bin/STARlong-ssse3", "ciri3": "/usr/local/bin/ciri3", "gmake": "/usr/local/bin/gmake", "inclusion_level.py": "/usr/local/bin/inclusion_level.py", "joinFiles.py": "/usr/local/bin/joinFiles.py", "paste.py": "/usr/local/bin/paste.py", "rmats.py": "/usr/local/bin/rmats.py", "STAR": "/usr/local/bin/STAR", "STARlong": "/usr/local/bin/STARlong", "jnativescan": "/usr/local/bin/jnativescan", "fc-genconf": "/usr/local/bin/fc-genconf", "jwebserver": "/usr/local/bin/jwebserver", "ref-cache": "/usr/local/bin/ref-cache", "jpackage": "/usr/local/bin/jpackage", "annot-tsv": "/usr/local/bin/annot-tsv", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "jfr": "/usr/local/bin/jfr", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink", "jmod": "/usr/local/bin/jmod", "jshell": "/usr/local/bin/jshell", "aserver": "/usr/local/bin/aserver", "jdeps": "/usr/local/bin/jdeps"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ciri3.
singularity registry hpc automated addition for ciri3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ciri3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ciri3:3.0.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ciri3/3.0.1--hdfd78af_0
$ module help quay.io/biocontainers/ciri3/3.0.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ciri3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ciri3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ciri3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ciri3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ciri3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ciri3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FDR.py

```bash
$ singularity exec <container> /usr/local/bin/FDR.py
$ podman run --it --rm --entrypoint /usr/local/bin/FDR.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FDR.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNASeq-MATS.py

```bash
$ singularity exec <container> /usr/local/bin/RNASeq-MATS.py
$ podman run --it --rm --entrypoint /usr/local/bin/RNASeq-MATS.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNASeq-MATS.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-avx

```bash
$ singularity exec <container> /usr/local/bin/STAR-avx
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-avx2

```bash
$ singularity exec <container> /usr/local/bin/STAR-avx2
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-plain

```bash
$ singularity exec <container> /usr/local/bin/STAR-plain
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-plain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-plain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-sse3

```bash
$ singularity exec <container> /usr/local/bin/STAR-sse3
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-sse3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-sse3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-sse4.1

```bash
$ singularity exec <container> /usr/local/bin/STAR-sse4.1
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-ssse3

```bash
$ singularity exec <container> /usr/local/bin/STAR-ssse3
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-ssse3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-ssse3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-avx

```bash
$ singularity exec <container> /usr/local/bin/STARlong-avx
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-avx2

```bash
$ singularity exec <container> /usr/local/bin/STARlong-avx2
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-plain

```bash
$ singularity exec <container> /usr/local/bin/STARlong-plain
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-plain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-plain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-sse3

```bash
$ singularity exec <container> /usr/local/bin/STARlong-sse3
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-sse3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-sse3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-sse4.1

```bash
$ singularity exec <container> /usr/local/bin/STARlong-sse4.1
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-ssse3

```bash
$ singularity exec <container> /usr/local/bin/STARlong-ssse3
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-ssse3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-ssse3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ciri3

```bash
$ singularity exec <container> /usr/local/bin/ciri3
$ podman run --it --rm --entrypoint /usr/local/bin/ciri3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ciri3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmake

```bash
$ singularity exec <container> /usr/local/bin/gmake
$ podman run --it --rm --entrypoint /usr/local/bin/gmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### inclusion_level.py

```bash
$ singularity exec <container> /usr/local/bin/inclusion_level.py
$ podman run --it --rm --entrypoint /usr/local/bin/inclusion_level.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/inclusion_level.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### joinFiles.py

```bash
$ singularity exec <container> /usr/local/bin/joinFiles.py
$ podman run --it --rm --entrypoint /usr/local/bin/joinFiles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/joinFiles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paste.py

```bash
$ singularity exec <container> /usr/local/bin/paste.py
$ podman run --it --rm --entrypoint /usr/local/bin/paste.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paste.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmats.py

```bash
$ singularity exec <container> /usr/local/bin/rmats.py
$ podman run --it --rm --entrypoint /usr/local/bin/rmats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR

```bash
$ singularity exec <container> /usr/local/bin/STAR
$ podman run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong

```bash
$ singularity exec <container> /usr/local/bin/STARlong
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jnativescan

```bash
$ singularity exec <container> /usr/local/bin/jnativescan
$ podman run --it --rm --entrypoint /usr/local/bin/jnativescan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jnativescan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jwebserver

```bash
$ singularity exec <container> /usr/local/bin/jwebserver
$ podman run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cups-config

```bash
$ singularity exec <container> /usr/local/bin/cups-config
$ podman run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ippeveprinter

```bash
$ singularity exec <container> /usr/local/bin/ippeveprinter
$ podman run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipptool

```bash
$ singularity exec <container> /usr/local/bin/ipptool
$ podman run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/local/bin/jlink
$ podman run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmod

```bash
$ singularity exec <container> /usr/local/bin/jmod
$ podman run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jshell

```bash
$ singularity exec <container> /usr/local/bin/jshell
$ podman run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeps

```bash
$ singularity exec <container> /usr/local/bin/jdeps
$ podman run --it --rm --entrypoint /usr/local/bin/jdeps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeps   -v ${PWD} -w ${PWD} <container> -c " $@"
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