---
layout: container
name:  "quay.io/biocontainers/biobb_md"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_md/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_md/container.yaml"
updated_at: "2023-11-21 02:43:45.975720"
latest: "3.7.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biobb_md"
aliases:
 - "GMXRC"
 - "GMXRC.bash"
 - "GMXRC.csh"
 - "GMXRC.zsh"
 - "append_ligand"
 - "demux.pl"
 - "editconf"
 - "genion"
 - "genrestr"
 - "gmx"
 - "gmx-completion-gmx.bash"
 - "gmx-completion.bash"
 - "gmxselect"
 - "grompp"
 - "grompp_mdrun"
 - "hwloc-annotate"
 - "hwloc-bind"
 - "hwloc-calc"
 - "hwloc-compress-dir"
 - "hwloc-diff"
 - "hwloc-distrib"
 - "hwloc-gather-cpuid"
 - "hwloc-gather-topology"
 - "hwloc-info"
 - "hwloc-ls"
 - "hwloc-patch"
 - "hwloc-ps"
 - "lstopo"
 - "lstopo-no-graphics"
 - "make_ndx"
 - "mdrun"
 - "ndx2resttop"
 - "pdb2gmx"
 - "solvate"
 - "xplor2gmx.pl"
 - "fftw-wisdom"
 - "fftw-wisdom-to-conf"
 - "fftwf-wisdom"
 - "fftwl-wisdom"
 - "normalizer"
 - "f2py3.7"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
versions:
 - "3.7.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for biobb_md"
config: {"url": "https://biocontainers.pro/tools/biobb_md", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobb_md", "latest": {"3.7.2--pyhdfd78af_0": "sha256:c143b11761a0b7ae12d954e40310aea41ccd8f3499761a8b070c165c216aeb96"}, "tags": {"3.7.2--pyhdfd78af_0": "sha256:c143b11761a0b7ae12d954e40310aea41ccd8f3499761a8b070c165c216aeb96"}, "docker": "quay.io/biocontainers/biobb_md", "aliases": {"GMXRC": "/usr/local/bin/GMXRC", "GMXRC.bash": "/usr/local/bin/GMXRC.bash", "GMXRC.csh": "/usr/local/bin/GMXRC.csh", "GMXRC.zsh": "/usr/local/bin/GMXRC.zsh", "append_ligand": "/usr/local/bin/append_ligand", "demux.pl": "/usr/local/bin/demux.pl", "editconf": "/usr/local/bin/editconf", "genion": "/usr/local/bin/genion", "genrestr": "/usr/local/bin/genrestr", "gmx": "/usr/local/bin/gmx", "gmx-completion-gmx.bash": "/usr/local/bin/gmx-completion-gmx.bash", "gmx-completion.bash": "/usr/local/bin/gmx-completion.bash", "gmxselect": "/usr/local/bin/gmxselect", "grompp": "/usr/local/bin/grompp", "grompp_mdrun": "/usr/local/bin/grompp_mdrun", "hwloc-annotate": "/usr/local/bin/hwloc-annotate", "hwloc-bind": "/usr/local/bin/hwloc-bind", "hwloc-calc": "/usr/local/bin/hwloc-calc", "hwloc-compress-dir": "/usr/local/bin/hwloc-compress-dir", "hwloc-diff": "/usr/local/bin/hwloc-diff", "hwloc-distrib": "/usr/local/bin/hwloc-distrib", "hwloc-gather-cpuid": "/usr/local/bin/hwloc-gather-cpuid", "hwloc-gather-topology": "/usr/local/bin/hwloc-gather-topology", "hwloc-info": "/usr/local/bin/hwloc-info", "hwloc-ls": "/usr/local/bin/hwloc-ls", "hwloc-patch": "/usr/local/bin/hwloc-patch", "hwloc-ps": "/usr/local/bin/hwloc-ps", "lstopo": "/usr/local/bin/lstopo", "lstopo-no-graphics": "/usr/local/bin/lstopo-no-graphics", "make_ndx": "/usr/local/bin/make_ndx", "mdrun": "/usr/local/bin/mdrun", "ndx2resttop": "/usr/local/bin/ndx2resttop", "pdb2gmx": "/usr/local/bin/pdb2gmx", "solvate": "/usr/local/bin/solvate", "xplor2gmx.pl": "/usr/local/bin/xplor2gmx.pl", "fftw-wisdom": "/usr/local/bin/fftw-wisdom", "fftw-wisdom-to-conf": "/usr/local/bin/fftw-wisdom-to-conf", "fftwf-wisdom": "/usr/local/bin/fftwf-wisdom", "fftwl-wisdom": "/usr/local/bin/fftwl-wisdom", "normalizer": "/usr/local/bin/normalizer", "f2py3.7": "/usr/local/bin/f2py3.7", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_md.
shpc-registry automated BioContainers addition for biobb_md
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_md
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_md:3.7.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_md/3.7.2--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_md/3.7.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_md-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_md-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_md-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_md-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_md-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_md-inspect-deffile:

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


#### append_ligand

```bash
$ singularity exec <container> /usr/local/bin/append_ligand
$ podman run --it --rm --entrypoint /usr/local/bin/append_ligand   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/append_ligand   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### demux.pl

```bash
$ singularity exec <container> /usr/local/bin/demux.pl
$ podman run --it --rm --entrypoint /usr/local/bin/demux.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demux.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### editconf

```bash
$ singularity exec <container> /usr/local/bin/editconf
$ podman run --it --rm --entrypoint /usr/local/bin/editconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/editconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genion

```bash
$ singularity exec <container> /usr/local/bin/genion
$ podman run --it --rm --entrypoint /usr/local/bin/genion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genrestr

```bash
$ singularity exec <container> /usr/local/bin/genrestr
$ podman run --it --rm --entrypoint /usr/local/bin/genrestr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genrestr   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gmxselect

```bash
$ singularity exec <container> /usr/local/bin/gmxselect
$ podman run --it --rm --entrypoint /usr/local/bin/gmxselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmxselect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grompp

```bash
$ singularity exec <container> /usr/local/bin/grompp
$ podman run --it --rm --entrypoint /usr/local/bin/grompp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grompp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grompp_mdrun

```bash
$ singularity exec <container> /usr/local/bin/grompp_mdrun
$ podman run --it --rm --entrypoint /usr/local/bin/grompp_mdrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grompp_mdrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-annotate

```bash
$ singularity exec <container> /usr/local/bin/hwloc-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### hwloc-distrib

```bash
$ singularity exec <container> /usr/local/bin/hwloc-distrib
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-gather-cpuid

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-cpuid
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### make_ndx

```bash
$ singularity exec <container> /usr/local/bin/make_ndx
$ podman run --it --rm --entrypoint /usr/local/bin/make_ndx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_ndx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mdrun

```bash
$ singularity exec <container> /usr/local/bin/mdrun
$ podman run --it --rm --entrypoint /usr/local/bin/mdrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mdrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ndx2resttop

```bash
$ singularity exec <container> /usr/local/bin/ndx2resttop
$ podman run --it --rm --entrypoint /usr/local/bin/ndx2resttop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ndx2resttop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb2gmx

```bash
$ singularity exec <container> /usr/local/bin/pdb2gmx
$ podman run --it --rm --entrypoint /usr/local/bin/pdb2gmx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb2gmx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### solvate

```bash
$ singularity exec <container> /usr/local/bin/solvate
$ podman run --it --rm --entrypoint /usr/local/bin/solvate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/solvate   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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