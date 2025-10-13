---
layout: container
name:  "quay.io/biocontainers/pgap2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pgap2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pgap2/container.yaml"
updated_at: "2025-10-13 03:59:16.704989"
latest: "1.0.6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pgap2"
aliases:
 - "ClonalFrameML"
 - "RNAconsensus"
 - "clipkit"
 - "fitsverify"
 - "gdal_footprint"
 - "minigzip"
 - "miniprot"
 - "minizip"
 - "pgap2"
 - "rcl"
 - "rcl-dot-resmap.pl"
 - "rcl-qc"
 - "rcl-qm.R"
 - "rcl-relevel.pl"
 - "rcl-select.pl"
 - "rcldo.pl"
 - "run_fastbaps"
 - "tajimas_d"
 - "asn1Coding"
 - "asn1Decoding"
 - "asn1Parser"
 - "p11-kit"
 - "p11tool"
 - "sozip"
 - "trust"
 - "gawk-5.3.1"
 - "bsdunzip"
 - "raxml-ng"
 - "raxml-ng-mpi"
 - "TMalign"
 - "make_pscores.pl"
 - "poa"
 - "iqtree2"
 - "mclblastline"
 - "mcxdeblast"
 - "clm"
 - "clxdo"
 - "mcl"
 - "mcx"
 - "mcxarray"
 - "mcxdump"
 - "mcxi"
 - "mcxload"
versions:
 - "1.0.3--pyhdfd78af_0"
 - "1.0.4--pyhdfd78af_0"
 - "1.0.6--pyhdfd78af_0"
description: "singularity registry hpc automated addition for pgap2"
config: {"url": "https://biocontainers.pro/tools/pgap2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pgap2", "latest": {"1.0.6--pyhdfd78af_0": "sha256:40b46f57b1ea861d1d30e1b6fc0df3c149b6c82721b27f38af4f2f39aa193369"}, "tags": {"1.0.3--pyhdfd78af_0": "sha256:aed887ef1ac44e627739a0bacba705ce04cb51437289f669a686af6c1e1540de", "1.0.4--pyhdfd78af_0": "sha256:839d7eb05b5ed6a903d4f32b60bd61ebb0e2af923b96754c11465ea56efba292", "1.0.6--pyhdfd78af_0": "sha256:40b46f57b1ea861d1d30e1b6fc0df3c149b6c82721b27f38af4f2f39aa193369"}, "docker": "quay.io/biocontainers/pgap2", "aliases": {"ClonalFrameML": "/usr/local/bin/ClonalFrameML", "RNAconsensus": "/usr/local/bin/RNAconsensus", "clipkit": "/usr/local/bin/clipkit", "fitsverify": "/usr/local/bin/fitsverify", "gdal_footprint": "/usr/local/bin/gdal_footprint", "minigzip": "/usr/local/bin/minigzip", "miniprot": "/usr/local/bin/miniprot", "minizip": "/usr/local/bin/minizip", "pgap2": "/usr/local/bin/pgap2", "rcl": "/usr/local/bin/rcl", "rcl-dot-resmap.pl": "/usr/local/bin/rcl-dot-resmap.pl", "rcl-qc": "/usr/local/bin/rcl-qc", "rcl-qm.R": "/usr/local/bin/rcl-qm.R", "rcl-relevel.pl": "/usr/local/bin/rcl-relevel.pl", "rcl-select.pl": "/usr/local/bin/rcl-select.pl", "rcldo.pl": "/usr/local/bin/rcldo.pl", "run_fastbaps": "/usr/local/bin/run_fastbaps", "tajimas_d": "/usr/local/bin/tajimas_d", "asn1Coding": "/usr/local/bin/asn1Coding", "asn1Decoding": "/usr/local/bin/asn1Decoding", "asn1Parser": "/usr/local/bin/asn1Parser", "p11-kit": "/usr/local/bin/p11-kit", "p11tool": "/usr/local/bin/p11tool", "sozip": "/usr/local/bin/sozip", "trust": "/usr/local/bin/trust", "gawk-5.3.1": "/usr/local/bin/gawk-5.3.1", "bsdunzip": "/usr/local/bin/bsdunzip", "raxml-ng": "/usr/local/bin/raxml-ng", "raxml-ng-mpi": "/usr/local/bin/raxml-ng-mpi", "TMalign": "/usr/local/bin/TMalign", "make_pscores.pl": "/usr/local/bin/make_pscores.pl", "poa": "/usr/local/bin/poa", "iqtree2": "/usr/local/bin/iqtree2", "mclblastline": "/usr/local/bin/mclblastline", "mcxdeblast": "/usr/local/bin/mcxdeblast", "clm": "/usr/local/bin/clm", "clxdo": "/usr/local/bin/clxdo", "mcl": "/usr/local/bin/mcl", "mcx": "/usr/local/bin/mcx", "mcxarray": "/usr/local/bin/mcxarray", "mcxdump": "/usr/local/bin/mcxdump", "mcxi": "/usr/local/bin/mcxi", "mcxload": "/usr/local/bin/mcxload"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pgap2.
singularity registry hpc automated addition for pgap2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pgap2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pgap2:1.0.6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pgap2/1.0.6--pyhdfd78af_0
$ module help quay.io/biocontainers/pgap2/1.0.6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pgap2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pgap2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pgap2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pgap2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pgap2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pgap2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ClonalFrameML

```bash
$ singularity exec <container> /usr/local/bin/ClonalFrameML
$ podman run --it --rm --entrypoint /usr/local/bin/ClonalFrameML   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ClonalFrameML   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAconsensus

```bash
$ singularity exec <container> /usr/local/bin/RNAconsensus
$ podman run --it --rm --entrypoint /usr/local/bin/RNAconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clipkit

```bash
$ singularity exec <container> /usr/local/bin/clipkit
$ podman run --it --rm --entrypoint /usr/local/bin/clipkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clipkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fitsverify

```bash
$ singularity exec <container> /usr/local/bin/fitsverify
$ podman run --it --rm --entrypoint /usr/local/bin/fitsverify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fitsverify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_footprint

```bash
$ singularity exec <container> /usr/local/bin/gdal_footprint
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_footprint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_footprint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minigzip

```bash
$ singularity exec <container> /usr/local/bin/minigzip
$ podman run --it --rm --entrypoint /usr/local/bin/minigzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minigzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miniprot

```bash
$ singularity exec <container> /usr/local/bin/miniprot
$ podman run --it --rm --entrypoint /usr/local/bin/miniprot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miniprot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minizip

```bash
$ singularity exec <container> /usr/local/bin/minizip
$ podman run --it --rm --entrypoint /usr/local/bin/minizip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minizip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgap2

```bash
$ singularity exec <container> /usr/local/bin/pgap2
$ podman run --it --rm --entrypoint /usr/local/bin/pgap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgap2   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### run_fastbaps

```bash
$ singularity exec <container> /usr/local/bin/run_fastbaps
$ podman run --it --rm --entrypoint /usr/local/bin/run_fastbaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_fastbaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tajimas_d

```bash
$ singularity exec <container> /usr/local/bin/tajimas_d
$ podman run --it --rm --entrypoint /usr/local/bin/tajimas_d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tajimas_d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Coding

```bash
$ singularity exec <container> /usr/local/bin/asn1Coding
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Coding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Coding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Decoding

```bash
$ singularity exec <container> /usr/local/bin/asn1Decoding
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Decoding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Decoding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Parser

```bash
$ singularity exec <container> /usr/local/bin/asn1Parser
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Parser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Parser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### p11-kit

```bash
$ singularity exec <container> /usr/local/bin/p11-kit
$ podman run --it --rm --entrypoint /usr/local/bin/p11-kit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/p11-kit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### p11tool

```bash
$ singularity exec <container> /usr/local/bin/p11tool
$ podman run --it --rm --entrypoint /usr/local/bin/p11tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/p11tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sozip

```bash
$ singularity exec <container> /usr/local/bin/sozip
$ podman run --it --rm --entrypoint /usr/local/bin/sozip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sozip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trust

```bash
$ singularity exec <container> /usr/local/bin/trust
$ podman run --it --rm --entrypoint /usr/local/bin/trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdunzip

```bash
$ singularity exec <container> /usr/local/bin/bsdunzip
$ podman run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxml-ng

```bash
$ singularity exec <container> /usr/local/bin/raxml-ng
$ podman run --it --rm --entrypoint /usr/local/bin/raxml-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxml-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxml-ng-mpi

```bash
$ singularity exec <container> /usr/local/bin/raxml-ng-mpi
$ podman run --it --rm --entrypoint /usr/local/bin/raxml-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxml-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TMalign

```bash
$ singularity exec <container> /usr/local/bin/TMalign
$ podman run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_pscores.pl

```bash
$ singularity exec <container> /usr/local/bin/make_pscores.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_pscores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_pscores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### poa

```bash
$ singularity exec <container> /usr/local/bin/poa
$ podman run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iqtree2

```bash
$ singularity exec <container> /usr/local/bin/iqtree2
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclblastline

```bash
$ singularity exec <container> /usr/local/bin/mclblastline
$ podman run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxdeblast

```bash
$ singularity exec <container> /usr/local/bin/mcxdeblast
$ podman run --it --rm --entrypoint /usr/local/bin/mcxdeblast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxdeblast   -v ${PWD} -w ${PWD} <container> -c " $@"
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