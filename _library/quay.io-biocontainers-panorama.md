---
layout: container
name:  "quay.io/biocontainers/panorama"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/panorama/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/panorama/container.yaml"
updated_at: "2025-12-18 03:30:25.063593"
latest: "0.5.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/panorama"
aliases:
 - "geckodriver"
 - "panorama"
 - "ppanggolin"
 - "selenium-manager"
 - "archspec"
 - "wsdump"
 - "cpuinfo"
 - "pyrodigal"
 - "gawk-5.3.1"
 - "aragorn"
 - "aria2c"
 - "h5fuse"
 - "mmseqs"
 - "cmalign"
 - "cmbuild"
 - "cmcalibrate"
 - "cmconvert"
 - "cmemit"
 - "cmfetch"
 - "cmpress"
 - "cmscan"
 - "cmsearch"
 - "cmstat"
 - "gawkbug"
 - "pt2to3"
 - "ptdump"
 - "ptrepack"
 - "pttree"
 - "bokeh"
versions:
 - "0.5.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for panorama"
config: {"url": "https://biocontainers.pro/tools/panorama", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for panorama", "latest": {"0.5.0--pyhdfd78af_0": "sha256:3b08a1ff06973876cc7719bab7379c66e4c85d74e245c16b75260895b1bdf255"}, "tags": {"0.5.0--pyhdfd78af_0": "sha256:3b08a1ff06973876cc7719bab7379c66e4c85d74e245c16b75260895b1bdf255"}, "docker": "quay.io/biocontainers/panorama", "aliases": {"geckodriver": "/usr/local/bin/geckodriver", "panorama": "/usr/local/bin/panorama", "ppanggolin": "/usr/local/bin/ppanggolin", "selenium-manager": "/usr/local/bin/selenium-manager", "archspec": "/usr/local/bin/archspec", "wsdump": "/usr/local/bin/wsdump", "cpuinfo": "/usr/local/bin/cpuinfo", "pyrodigal": "/usr/local/bin/pyrodigal", "gawk-5.3.1": "/usr/local/bin/gawk-5.3.1", "aragorn": "/usr/local/bin/aragorn", "aria2c": "/usr/local/bin/aria2c", "h5fuse": "/usr/local/bin/h5fuse", "mmseqs": "/usr/local/bin/mmseqs", "cmalign": "/usr/local/bin/cmalign", "cmbuild": "/usr/local/bin/cmbuild", "cmcalibrate": "/usr/local/bin/cmcalibrate", "cmconvert": "/usr/local/bin/cmconvert", "cmemit": "/usr/local/bin/cmemit", "cmfetch": "/usr/local/bin/cmfetch", "cmpress": "/usr/local/bin/cmpress", "cmscan": "/usr/local/bin/cmscan", "cmsearch": "/usr/local/bin/cmsearch", "cmstat": "/usr/local/bin/cmstat", "gawkbug": "/usr/local/bin/gawkbug", "pt2to3": "/usr/local/bin/pt2to3", "ptdump": "/usr/local/bin/ptdump", "ptrepack": "/usr/local/bin/ptrepack", "pttree": "/usr/local/bin/pttree", "bokeh": "/usr/local/bin/bokeh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/panorama.
singularity registry hpc automated addition for panorama
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/panorama
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/panorama:0.5.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/panorama/0.5.0--pyhdfd78af_0
$ module help quay.io/biocontainers/panorama/0.5.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### panorama-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### panorama-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### panorama-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### panorama-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### panorama-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### panorama-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### geckodriver

```bash
$ singularity exec <container> /usr/local/bin/geckodriver
$ podman run --it --rm --entrypoint /usr/local/bin/geckodriver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geckodriver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### panorama

```bash
$ singularity exec <container> /usr/local/bin/panorama
$ podman run --it --rm --entrypoint /usr/local/bin/panorama   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/panorama   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanggolin

```bash
$ singularity exec <container> /usr/local/bin/ppanggolin
$ podman run --it --rm --entrypoint /usr/local/bin/ppanggolin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanggolin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### selenium-manager

```bash
$ singularity exec <container> /usr/local/bin/selenium-manager
$ podman run --it --rm --entrypoint /usr/local/bin/selenium-manager   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/selenium-manager   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archspec

```bash
$ singularity exec <container> /usr/local/bin/archspec
$ podman run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpuinfo

```bash
$ singularity exec <container> /usr/local/bin/cpuinfo
$ podman run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrodigal

```bash
$ singularity exec <container> /usr/local/bin/pyrodigal
$ podman run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aragorn

```bash
$ singularity exec <container> /usr/local/bin/aragorn
$ podman run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aria2c

```bash
$ singularity exec <container> /usr/local/bin/aria2c
$ podman run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse

```bash
$ singularity exec <container> /usr/local/bin/h5fuse
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmseqs

```bash
$ singularity exec <container> /usr/local/bin/mmseqs
$ podman run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### cmemit

```bash
$ singularity exec <container> /usr/local/bin/cmemit
$ podman run --it --rm --entrypoint /usr/local/bin/cmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmfetch

```bash
$ singularity exec <container> /usr/local/bin/cmfetch
$ podman run --it --rm --entrypoint /usr/local/bin/cmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmpress

```bash
$ singularity exec <container> /usr/local/bin/cmpress
$ podman run --it --rm --entrypoint /usr/local/bin/cmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmscan

```bash
$ singularity exec <container> /usr/local/bin/cmscan
$ podman run --it --rm --entrypoint /usr/local/bin/cmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmsearch

```bash
$ singularity exec <container> /usr/local/bin/cmsearch
$ podman run --it --rm --entrypoint /usr/local/bin/cmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmstat

```bash
$ singularity exec <container> /usr/local/bin/cmstat
$ podman run --it --rm --entrypoint /usr/local/bin/cmstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pt2to3

```bash
$ singularity exec <container> /usr/local/bin/pt2to3
$ podman run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptdump

```bash
$ singularity exec <container> /usr/local/bin/ptdump
$ podman run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptrepack

```bash
$ singularity exec <container> /usr/local/bin/ptrepack
$ podman run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pttree

```bash
$ singularity exec <container> /usr/local/bin/pttree
$ podman run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bokeh

```bash
$ singularity exec <container> /usr/local/bin/bokeh
$ podman run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
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