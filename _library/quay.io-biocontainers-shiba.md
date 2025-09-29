---
layout: container
name:  "quay.io/biocontainers/shiba"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/shiba/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/shiba/container.yaml"
updated_at: "2025-09-29 03:21:37.702888"
latest: "0.7.1--py313hdfd78af_0"
container_url: "https://biocontainers.pro/tools/shiba"
aliases:
 - "flattenGTF"
 - "genRandomReads"
 - "prepDE.py"
 - "propmapped"
 - "qualityScores"
 - "regtools"
 - "removeDup"
 - "repair"
 - "scshiba.py"
 - "shiba.py"
 - "stringtie"
 - "sublong"
 - "subread-fullscan"
 - "exactSNP"
 - "featureCounts"
 - "subindel"
 - "subjunc"
 - "subread-align"
 - "subread-buildindex"
 - "h5fuse"
 - "scanpy"
 - "annot-tsv"
 - "x86_64-conda-linux-gnu.cfg"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "hwloc-gather-cpuid"
 - "hwloc-annotate"
 - "hwloc-bind"
 - "hwloc-calc"
 - "hwloc-compress-dir"
 - "hwloc-diff"
 - "hwloc-distrib"
 - "hwloc-gather-topology"
 - "hwloc-info"
versions:
 - "0.6.1--py313hdfd78af_0"
 - "0.6.2--py313hdfd78af_0"
 - "0.6.3--py313hdfd78af_0"
 - "0.7.1--py313hdfd78af_0"
description: "singularity registry hpc automated addition for shiba"
config: {"url": "https://biocontainers.pro/tools/shiba", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for shiba", "latest": {"0.7.1--py313hdfd78af_0": "sha256:87abbe5df253a34d2ed551f078e471de299196ea93dbe16e1a12ac00e01706b2"}, "tags": {"0.6.1--py313hdfd78af_0": "sha256:504a469d9fefc584a465b2360d3d2ddf51c65298eaa012cae310379b826e1a9c", "0.6.2--py313hdfd78af_0": "sha256:1cad5e25b1391b4929b1b63eb6d28a209087b39834eb73e0718f1275d31ad3c1", "0.6.3--py313hdfd78af_0": "sha256:48302cb2a0b0b2eafc3a6a3cbcb465693501dfbdf54467e7b2e7087986b26eda", "0.7.1--py313hdfd78af_0": "sha256:87abbe5df253a34d2ed551f078e471de299196ea93dbe16e1a12ac00e01706b2"}, "docker": "quay.io/biocontainers/shiba", "aliases": {"flattenGTF": "/usr/local/bin/flattenGTF", "genRandomReads": "/usr/local/bin/genRandomReads", "prepDE.py": "/usr/local/bin/prepDE.py", "propmapped": "/usr/local/bin/propmapped", "qualityScores": "/usr/local/bin/qualityScores", "regtools": "/usr/local/bin/regtools", "removeDup": "/usr/local/bin/removeDup", "repair": "/usr/local/bin/repair", "scshiba.py": "/usr/local/bin/scshiba.py", "shiba.py": "/usr/local/bin/shiba.py", "stringtie": "/usr/local/bin/stringtie", "sublong": "/usr/local/bin/sublong", "subread-fullscan": "/usr/local/bin/subread-fullscan", "exactSNP": "/usr/local/bin/exactSNP", "featureCounts": "/usr/local/bin/featureCounts", "subindel": "/usr/local/bin/subindel", "subjunc": "/usr/local/bin/subjunc", "subread-align": "/usr/local/bin/subread-align", "subread-buildindex": "/usr/local/bin/subread-buildindex", "h5fuse": "/usr/local/bin/h5fuse", "scanpy": "/usr/local/bin/scanpy", "annot-tsv": "/usr/local/bin/annot-tsv", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "hwloc-gather-cpuid": "/usr/local/bin/hwloc-gather-cpuid", "hwloc-annotate": "/usr/local/bin/hwloc-annotate", "hwloc-bind": "/usr/local/bin/hwloc-bind", "hwloc-calc": "/usr/local/bin/hwloc-calc", "hwloc-compress-dir": "/usr/local/bin/hwloc-compress-dir", "hwloc-diff": "/usr/local/bin/hwloc-diff", "hwloc-distrib": "/usr/local/bin/hwloc-distrib", "hwloc-gather-topology": "/usr/local/bin/hwloc-gather-topology", "hwloc-info": "/usr/local/bin/hwloc-info"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/shiba.
singularity registry hpc automated addition for shiba
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/shiba
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/shiba:0.7.1--py313hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/shiba/0.7.1--py313hdfd78af_0
$ module help quay.io/biocontainers/shiba/0.7.1--py313hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### shiba-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### shiba-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### shiba-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### shiba-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### shiba-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### shiba-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### flattenGTF

```bash
$ singularity exec <container> /usr/local/bin/flattenGTF
$ podman run --it --rm --entrypoint /usr/local/bin/flattenGTF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flattenGTF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genRandomReads

```bash
$ singularity exec <container> /usr/local/bin/genRandomReads
$ podman run --it --rm --entrypoint /usr/local/bin/genRandomReads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genRandomReads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepDE.py

```bash
$ singularity exec <container> /usr/local/bin/prepDE.py
$ podman run --it --rm --entrypoint /usr/local/bin/prepDE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepDE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### propmapped

```bash
$ singularity exec <container> /usr/local/bin/propmapped
$ podman run --it --rm --entrypoint /usr/local/bin/propmapped   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/propmapped   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualityScores

```bash
$ singularity exec <container> /usr/local/bin/qualityScores
$ podman run --it --rm --entrypoint /usr/local/bin/qualityScores   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualityScores   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### regtools

```bash
$ singularity exec <container> /usr/local/bin/regtools
$ podman run --it --rm --entrypoint /usr/local/bin/regtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/regtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### removeDup

```bash
$ singularity exec <container> /usr/local/bin/removeDup
$ podman run --it --rm --entrypoint /usr/local/bin/removeDup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/removeDup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repair

```bash
$ singularity exec <container> /usr/local/bin/repair
$ podman run --it --rm --entrypoint /usr/local/bin/repair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scshiba.py

```bash
$ singularity exec <container> /usr/local/bin/scshiba.py
$ podman run --it --rm --entrypoint /usr/local/bin/scshiba.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scshiba.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiba.py

```bash
$ singularity exec <container> /usr/local/bin/shiba.py
$ podman run --it --rm --entrypoint /usr/local/bin/shiba.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiba.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stringtie

```bash
$ singularity exec <container> /usr/local/bin/stringtie
$ podman run --it --rm --entrypoint /usr/local/bin/stringtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stringtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sublong

```bash
$ singularity exec <container> /usr/local/bin/sublong
$ podman run --it --rm --entrypoint /usr/local/bin/sublong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sublong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subread-fullscan

```bash
$ singularity exec <container> /usr/local/bin/subread-fullscan
$ podman run --it --rm --entrypoint /usr/local/bin/subread-fullscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subread-fullscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exactSNP

```bash
$ singularity exec <container> /usr/local/bin/exactSNP
$ podman run --it --rm --entrypoint /usr/local/bin/exactSNP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exactSNP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### featureCounts

```bash
$ singularity exec <container> /usr/local/bin/featureCounts
$ podman run --it --rm --entrypoint /usr/local/bin/featureCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/featureCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subindel

```bash
$ singularity exec <container> /usr/local/bin/subindel
$ podman run --it --rm --entrypoint /usr/local/bin/subindel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subindel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subjunc

```bash
$ singularity exec <container> /usr/local/bin/subjunc
$ podman run --it --rm --entrypoint /usr/local/bin/subjunc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subjunc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subread-align

```bash
$ singularity exec <container> /usr/local/bin/subread-align
$ podman run --it --rm --entrypoint /usr/local/bin/subread-align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subread-align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subread-buildindex

```bash
$ singularity exec <container> /usr/local/bin/subread-buildindex
$ podman run --it --rm --entrypoint /usr/local/bin/subread-buildindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subread-buildindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse

```bash
$ singularity exec <container> /usr/local/bin/h5fuse
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy

```bash
$ singularity exec <container> /usr/local/bin/scanpy
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qconvex

```bash
$ singularity exec <container> /usr/local/bin/qconvex
$ podman run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdelaunay

```bash
$ singularity exec <container> /usr/local/bin/qdelaunay
$ podman run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhalf

```bash
$ singularity exec <container> /usr/local/bin/qhalf
$ podman run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhull

```bash
$ singularity exec <container> /usr/local/bin/qhull
$ podman run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvoronoi

```bash
$ singularity exec <container> /usr/local/bin/qvoronoi
$ podman run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbox

```bash
$ singularity exec <container> /usr/local/bin/rbox
$ podman run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-gather-cpuid

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-cpuid
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
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