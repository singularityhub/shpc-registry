---
layout: container
name:  "quay.io/biocontainers/obitools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/obitools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/obitools/container.yaml"
updated_at: "2025-12-08 05:23:17.378383"
latest: "1.2.13--py27h9801fc8_4"
container_url: "https://biocontainers.pro/tools/obitools"
aliases:
 - "ali2consensus"
 - "ecodbtaxstat"
 - "ecotag"
 - "ecotaxspecificity"
 - "ecotaxstat"
 - "extractreads"
 - "extractreads2"
 - "illuminapairedend"
 - "iptest2"
 - "ipython2"
 - "ngsfilter"
 - "obiaddtaxids"
 - "obiannotate"
 - "obiclean"
 - "obicomplement"
 - "obiconvert"
 - "obicount"
 - "obicut"
 - "obidistribute"
 - "obiextract"
 - "obigrep"
 - "obihead"
 - "obijoinpairedend"
 - "obipr2"
 - "obisample"
 - "obiselect"
 - "obisilva"
 - "obisort"
 - "obisplit"
 - "obistat"
 - "obisubset"
 - "obitab"
 - "obitail"
 - "obitaxonomy"
 - "obiuniq"
 - "oligotag"
 - "iptest"
 - "ipython"
 - "pygmentize"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "1.2.13--py27h9801fc8_4"
description: "shpc-registry automated BioContainers addition for obitools"
config: {"url": "https://biocontainers.pro/tools/obitools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for obitools", "latest": {"1.2.13--py27h9801fc8_4": "sha256:c71ee5146f362c785d9edd05be7b4a0b7b5e101ff42a7a912734ca746a988fb4"}, "tags": {"1.2.13--py27h9801fc8_4": "sha256:c71ee5146f362c785d9edd05be7b4a0b7b5e101ff42a7a912734ca746a988fb4"}, "docker": "quay.io/biocontainers/obitools", "aliases": {"ali2consensus": "/usr/local/bin/ali2consensus", "ecodbtaxstat": "/usr/local/bin/ecodbtaxstat", "ecotag": "/usr/local/bin/ecotag", "ecotaxspecificity": "/usr/local/bin/ecotaxspecificity", "ecotaxstat": "/usr/local/bin/ecotaxstat", "extractreads": "/usr/local/bin/extractreads", "extractreads2": "/usr/local/bin/extractreads2", "illuminapairedend": "/usr/local/bin/illuminapairedend", "iptest2": "/usr/local/bin/iptest2", "ipython2": "/usr/local/bin/ipython2", "ngsfilter": "/usr/local/bin/ngsfilter", "obiaddtaxids": "/usr/local/bin/obiaddtaxids", "obiannotate": "/usr/local/bin/obiannotate", "obiclean": "/usr/local/bin/obiclean", "obicomplement": "/usr/local/bin/obicomplement", "obiconvert": "/usr/local/bin/obiconvert", "obicount": "/usr/local/bin/obicount", "obicut": "/usr/local/bin/obicut", "obidistribute": "/usr/local/bin/obidistribute", "obiextract": "/usr/local/bin/obiextract", "obigrep": "/usr/local/bin/obigrep", "obihead": "/usr/local/bin/obihead", "obijoinpairedend": "/usr/local/bin/obijoinpairedend", "obipr2": "/usr/local/bin/obipr2", "obisample": "/usr/local/bin/obisample", "obiselect": "/usr/local/bin/obiselect", "obisilva": "/usr/local/bin/obisilva", "obisort": "/usr/local/bin/obisort", "obisplit": "/usr/local/bin/obisplit", "obistat": "/usr/local/bin/obistat", "obisubset": "/usr/local/bin/obisubset", "obitab": "/usr/local/bin/obitab", "obitail": "/usr/local/bin/obitail", "obitaxonomy": "/usr/local/bin/obitaxonomy", "obiuniq": "/usr/local/bin/obiuniq", "oligotag": "/usr/local/bin/oligotag", "iptest": "/usr/local/bin/iptest", "ipython": "/usr/local/bin/ipython", "pygmentize": "/usr/local/bin/pygmentize", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/obitools.
shpc-registry automated BioContainers addition for obitools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/obitools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/obitools:1.2.13--py27h9801fc8_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/obitools/1.2.13--py27h9801fc8_4
$ module help quay.io/biocontainers/obitools/1.2.13--py27h9801fc8_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### obitools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### obitools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### obitools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### obitools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### obitools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### obitools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ali2consensus

```bash
$ singularity exec <container> /usr/local/bin/ali2consensus
$ podman run --it --rm --entrypoint /usr/local/bin/ali2consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ali2consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecodbtaxstat

```bash
$ singularity exec <container> /usr/local/bin/ecodbtaxstat
$ podman run --it --rm --entrypoint /usr/local/bin/ecodbtaxstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecodbtaxstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecotag

```bash
$ singularity exec <container> /usr/local/bin/ecotag
$ podman run --it --rm --entrypoint /usr/local/bin/ecotag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecotag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecotaxspecificity

```bash
$ singularity exec <container> /usr/local/bin/ecotaxspecificity
$ podman run --it --rm --entrypoint /usr/local/bin/ecotaxspecificity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecotaxspecificity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecotaxstat

```bash
$ singularity exec <container> /usr/local/bin/ecotaxstat
$ podman run --it --rm --entrypoint /usr/local/bin/ecotaxstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecotaxstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractreads

```bash
$ singularity exec <container> /usr/local/bin/extractreads
$ podman run --it --rm --entrypoint /usr/local/bin/extractreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractreads2

```bash
$ singularity exec <container> /usr/local/bin/extractreads2
$ podman run --it --rm --entrypoint /usr/local/bin/extractreads2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractreads2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### illuminapairedend

```bash
$ singularity exec <container> /usr/local/bin/illuminapairedend
$ podman run --it --rm --entrypoint /usr/local/bin/illuminapairedend   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/illuminapairedend   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iptest2

```bash
$ singularity exec <container> /usr/local/bin/iptest2
$ podman run --it --rm --entrypoint /usr/local/bin/iptest2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython2

```bash
$ singularity exec <container> /usr/local/bin/ipython2
$ podman run --it --rm --entrypoint /usr/local/bin/ipython2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngsfilter

```bash
$ singularity exec <container> /usr/local/bin/ngsfilter
$ podman run --it --rm --entrypoint /usr/local/bin/ngsfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngsfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obiaddtaxids

```bash
$ singularity exec <container> /usr/local/bin/obiaddtaxids
$ podman run --it --rm --entrypoint /usr/local/bin/obiaddtaxids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obiaddtaxids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obiannotate

```bash
$ singularity exec <container> /usr/local/bin/obiannotate
$ podman run --it --rm --entrypoint /usr/local/bin/obiannotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obiannotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obiclean

```bash
$ singularity exec <container> /usr/local/bin/obiclean
$ podman run --it --rm --entrypoint /usr/local/bin/obiclean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obiclean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obicomplement

```bash
$ singularity exec <container> /usr/local/bin/obicomplement
$ podman run --it --rm --entrypoint /usr/local/bin/obicomplement   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obicomplement   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obiconvert

```bash
$ singularity exec <container> /usr/local/bin/obiconvert
$ podman run --it --rm --entrypoint /usr/local/bin/obiconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obiconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obicount

```bash
$ singularity exec <container> /usr/local/bin/obicount
$ podman run --it --rm --entrypoint /usr/local/bin/obicount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obicount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obicut

```bash
$ singularity exec <container> /usr/local/bin/obicut
$ podman run --it --rm --entrypoint /usr/local/bin/obicut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obicut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obidistribute

```bash
$ singularity exec <container> /usr/local/bin/obidistribute
$ podman run --it --rm --entrypoint /usr/local/bin/obidistribute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obidistribute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obiextract

```bash
$ singularity exec <container> /usr/local/bin/obiextract
$ podman run --it --rm --entrypoint /usr/local/bin/obiextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obiextract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obigrep

```bash
$ singularity exec <container> /usr/local/bin/obigrep
$ podman run --it --rm --entrypoint /usr/local/bin/obigrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obigrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obihead

```bash
$ singularity exec <container> /usr/local/bin/obihead
$ podman run --it --rm --entrypoint /usr/local/bin/obihead   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obihead   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obijoinpairedend

```bash
$ singularity exec <container> /usr/local/bin/obijoinpairedend
$ podman run --it --rm --entrypoint /usr/local/bin/obijoinpairedend   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obijoinpairedend   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obipr2

```bash
$ singularity exec <container> /usr/local/bin/obipr2
$ podman run --it --rm --entrypoint /usr/local/bin/obipr2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obipr2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obisample

```bash
$ singularity exec <container> /usr/local/bin/obisample
$ podman run --it --rm --entrypoint /usr/local/bin/obisample   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obisample   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obiselect

```bash
$ singularity exec <container> /usr/local/bin/obiselect
$ podman run --it --rm --entrypoint /usr/local/bin/obiselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obiselect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obisilva

```bash
$ singularity exec <container> /usr/local/bin/obisilva
$ podman run --it --rm --entrypoint /usr/local/bin/obisilva   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obisilva   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obisort

```bash
$ singularity exec <container> /usr/local/bin/obisort
$ podman run --it --rm --entrypoint /usr/local/bin/obisort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obisort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obisplit

```bash
$ singularity exec <container> /usr/local/bin/obisplit
$ podman run --it --rm --entrypoint /usr/local/bin/obisplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obisplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obistat

```bash
$ singularity exec <container> /usr/local/bin/obistat
$ podman run --it --rm --entrypoint /usr/local/bin/obistat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obistat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obisubset

```bash
$ singularity exec <container> /usr/local/bin/obisubset
$ podman run --it --rm --entrypoint /usr/local/bin/obisubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obisubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obitab

```bash
$ singularity exec <container> /usr/local/bin/obitab
$ podman run --it --rm --entrypoint /usr/local/bin/obitab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obitab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obitail

```bash
$ singularity exec <container> /usr/local/bin/obitail
$ podman run --it --rm --entrypoint /usr/local/bin/obitail   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obitail   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obitaxonomy

```bash
$ singularity exec <container> /usr/local/bin/obitaxonomy
$ podman run --it --rm --entrypoint /usr/local/bin/obitaxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obitaxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obiuniq

```bash
$ singularity exec <container> /usr/local/bin/obiuniq
$ podman run --it --rm --entrypoint /usr/local/bin/obiuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obiuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oligotag

```bash
$ singularity exec <container> /usr/local/bin/oligotag
$ podman run --it --rm --entrypoint /usr/local/bin/oligotag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oligotag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iptest

```bash
$ singularity exec <container> /usr/local/bin/iptest
$ podman run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython

```bash
$ singularity exec <container> /usr/local/bin/ipython
$ podman run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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