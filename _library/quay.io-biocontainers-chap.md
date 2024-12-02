---
layout: container
name:  "quay.io/biocontainers/chap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chap/container.yaml"
updated_at: "2024-12-02 03:25:06.861387"
latest: "0.9.1--h2df963e_2"
container_url: "https://biocontainers.pro/tools/chap"
aliases:
 - "GMXRC"
 - "GMXRC.bash"
 - "GMXRC.csh"
 - "GMXRC.zsh"
 - "GenX_IR"
 - "chap"
 - "demux.pl"
 - "gmx"
 - "gmx-completion-gmx.bash"
 - "gmx-completion.bash"
 - "hwloc-annotate"
 - "hwloc-assembler"
 - "hwloc-assembler-remote"
 - "hwloc-bind"
 - "hwloc-calc"
 - "hwloc-compress-dir"
 - "hwloc-diff"
 - "hwloc-distances"
 - "hwloc-distrib"
 - "hwloc-gather-topology"
 - "hwloc-info"
 - "hwloc-ls"
 - "hwloc-patch"
 - "hwloc-ps"
 - "iga64"
 - "llvm-spirv"
 - "lstopo"
 - "lstopo-no-graphics"
 - "ocloc"
 - "xplor2gmx.pl"
 - "fftw-wisdom"
 - "fftw-wisdom-to-conf"
 - "fftwf-wisdom"
 - "fftwl-wisdom"
versions:
 - "0.9.1--h2df963e_2"
description: "shpc-registry automated BioContainers addition for chap"
config: {"url": "https://biocontainers.pro/tools/chap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chap", "latest": {"0.9.1--h2df963e_2": "sha256:13523b21b4073a71040b8e20a285571b4f5373a93646ed8624d70ac288ba6d98"}, "tags": {"0.9.1--h2df963e_2": "sha256:13523b21b4073a71040b8e20a285571b4f5373a93646ed8624d70ac288ba6d98"}, "docker": "quay.io/biocontainers/chap", "aliases": {"GMXRC": "/usr/local/bin/GMXRC", "GMXRC.bash": "/usr/local/bin/GMXRC.bash", "GMXRC.csh": "/usr/local/bin/GMXRC.csh", "GMXRC.zsh": "/usr/local/bin/GMXRC.zsh", "GenX_IR": "/usr/local/bin/GenX_IR", "chap": "/usr/local/bin/chap", "demux.pl": "/usr/local/bin/demux.pl", "gmx": "/usr/local/bin/gmx", "gmx-completion-gmx.bash": "/usr/local/bin/gmx-completion-gmx.bash", "gmx-completion.bash": "/usr/local/bin/gmx-completion.bash", "hwloc-annotate": "/usr/local/bin/hwloc-annotate", "hwloc-assembler": "/usr/local/bin/hwloc-assembler", "hwloc-assembler-remote": "/usr/local/bin/hwloc-assembler-remote", "hwloc-bind": "/usr/local/bin/hwloc-bind", "hwloc-calc": "/usr/local/bin/hwloc-calc", "hwloc-compress-dir": "/usr/local/bin/hwloc-compress-dir", "hwloc-diff": "/usr/local/bin/hwloc-diff", "hwloc-distances": "/usr/local/bin/hwloc-distances", "hwloc-distrib": "/usr/local/bin/hwloc-distrib", "hwloc-gather-topology": "/usr/local/bin/hwloc-gather-topology", "hwloc-info": "/usr/local/bin/hwloc-info", "hwloc-ls": "/usr/local/bin/hwloc-ls", "hwloc-patch": "/usr/local/bin/hwloc-patch", "hwloc-ps": "/usr/local/bin/hwloc-ps", "iga64": "/usr/local/bin/iga64", "llvm-spirv": "/usr/local/bin/llvm-spirv", "lstopo": "/usr/local/bin/lstopo", "lstopo-no-graphics": "/usr/local/bin/lstopo-no-graphics", "ocloc": "/usr/local/bin/ocloc", "xplor2gmx.pl": "/usr/local/bin/xplor2gmx.pl", "fftw-wisdom": "/usr/local/bin/fftw-wisdom", "fftw-wisdom-to-conf": "/usr/local/bin/fftw-wisdom-to-conf", "fftwf-wisdom": "/usr/local/bin/fftwf-wisdom", "fftwl-wisdom": "/usr/local/bin/fftwl-wisdom"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chap.
shpc-registry automated BioContainers addition for chap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chap:0.9.1--h2df963e_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chap/0.9.1--h2df963e_2
$ module help quay.io/biocontainers/chap/0.9.1--h2df963e_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GMXRC

```bash
$ singularity exec <container> /usr/local/bin/GMXRC
$ podman run --it --rm --entrypoint /usr/local/bin/GMXRC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GMXRC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GMXRC.bash

```bash
$ singularity exec <container> /usr/local/bin/GMXRC.bash
$ podman run --it --rm --entrypoint /usr/local/bin/GMXRC.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GMXRC.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GMXRC.csh

```bash
$ singularity exec <container> /usr/local/bin/GMXRC.csh
$ podman run --it --rm --entrypoint /usr/local/bin/GMXRC.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GMXRC.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GMXRC.zsh

```bash
$ singularity exec <container> /usr/local/bin/GMXRC.zsh
$ podman run --it --rm --entrypoint /usr/local/bin/GMXRC.zsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GMXRC.zsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GenX_IR

```bash
$ singularity exec <container> /usr/local/bin/GenX_IR
$ podman run --it --rm --entrypoint /usr/local/bin/GenX_IR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GenX_IR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chap

```bash
$ singularity exec <container> /usr/local/bin/chap
$ podman run --it --rm --entrypoint /usr/local/bin/chap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### demux.pl

```bash
$ singularity exec <container> /usr/local/bin/demux.pl
$ podman run --it --rm --entrypoint /usr/local/bin/demux.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demux.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmx

```bash
$ singularity exec <container> /usr/local/bin/gmx
$ podman run --it --rm --entrypoint /usr/local/bin/gmx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmx-completion-gmx.bash

```bash
$ singularity exec <container> /usr/local/bin/gmx-completion-gmx.bash
$ podman run --it --rm --entrypoint /usr/local/bin/gmx-completion-gmx.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmx-completion-gmx.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmx-completion.bash

```bash
$ singularity exec <container> /usr/local/bin/gmx-completion.bash
$ podman run --it --rm --entrypoint /usr/local/bin/gmx-completion.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmx-completion.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-annotate

```bash
$ singularity exec <container> /usr/local/bin/hwloc-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-assembler

```bash
$ singularity exec <container> /usr/local/bin/hwloc-assembler
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-assembler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-assembler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-assembler-remote

```bash
$ singularity exec <container> /usr/local/bin/hwloc-assembler-remote
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-assembler-remote   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-assembler-remote   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-bind

```bash
$ singularity exec <container> /usr/local/bin/hwloc-bind
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-calc

```bash
$ singularity exec <container> /usr/local/bin/hwloc-calc
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-compress-dir

```bash
$ singularity exec <container> /usr/local/bin/hwloc-compress-dir
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-compress-dir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-compress-dir   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-diff

```bash
$ singularity exec <container> /usr/local/bin/hwloc-diff
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-distances

```bash
$ singularity exec <container> /usr/local/bin/hwloc-distances
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-distances   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-distances   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-distrib

```bash
$ singularity exec <container> /usr/local/bin/hwloc-distrib
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-gather-topology

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-topology
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-topology   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-topology   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-info

```bash
$ singularity exec <container> /usr/local/bin/hwloc-info
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-ls

```bash
$ singularity exec <container> /usr/local/bin/hwloc-ls
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-patch

```bash
$ singularity exec <container> /usr/local/bin/hwloc-patch
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-patch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-patch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-ps

```bash
$ singularity exec <container> /usr/local/bin/hwloc-ps
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-ps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-ps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iga64

```bash
$ singularity exec <container> /usr/local/bin/iga64
$ podman run --it --rm --entrypoint /usr/local/bin/iga64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iga64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-spirv

```bash
$ singularity exec <container> /usr/local/bin/llvm-spirv
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-spirv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-spirv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lstopo

```bash
$ singularity exec <container> /usr/local/bin/lstopo
$ podman run --it --rm --entrypoint /usr/local/bin/lstopo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lstopo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lstopo-no-graphics

```bash
$ singularity exec <container> /usr/local/bin/lstopo-no-graphics
$ podman run --it --rm --entrypoint /usr/local/bin/lstopo-no-graphics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lstopo-no-graphics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocloc

```bash
$ singularity exec <container> /usr/local/bin/ocloc
$ podman run --it --rm --entrypoint /usr/local/bin/ocloc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocloc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xplor2gmx.pl

```bash
$ singularity exec <container> /usr/local/bin/xplor2gmx.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xplor2gmx.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xplor2gmx.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftw-wisdom

```bash
$ singularity exec <container> /usr/local/bin/fftw-wisdom
$ podman run --it --rm --entrypoint /usr/local/bin/fftw-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftw-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftw-wisdom-to-conf

```bash
$ singularity exec <container> /usr/local/bin/fftw-wisdom-to-conf
$ podman run --it --rm --entrypoint /usr/local/bin/fftw-wisdom-to-conf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftw-wisdom-to-conf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftwf-wisdom

```bash
$ singularity exec <container> /usr/local/bin/fftwf-wisdom
$ podman run --it --rm --entrypoint /usr/local/bin/fftwf-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftwf-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftwl-wisdom

```bash
$ singularity exec <container> /usr/local/bin/fftwl-wisdom
$ podman run --it --rm --entrypoint /usr/local/bin/fftwl-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftwl-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
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