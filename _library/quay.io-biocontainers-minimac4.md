---
layout: container
name:  "quay.io/biocontainers/minimac4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/minimac4/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/minimac4/container.yaml"
updated_at: "2025-12-13 04:00:12.292626"
latest: "4.1.6--hcb620b3_1"
container_url: "https://biocontainers.pro/tools/minimac4"
aliases:
 - "cget"
 - "edonr256-hash"
 - "edonr512-hash"
 - "gost12-256-hash"
 - "gost12-512-hash"
 - "minimac4"
 - "ccmake"
 - "cmake"
 - "cpack"
 - "ctest"
 - "ed2k-link"
 - "has160-hash"
 - "idle3.13"
 - "magnet-link"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "rhash"
 - "sfv-hash"
 - "tiger-hash"
 - "tth-hash"
 - "whirlpool-hash"
 - "annot-tsv"
 - "gff2gff.py"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "color-chrs.pl"
 - "plot-vcfstats"
 - "bcftools"
 - "vcfutils.pl"
versions:
 - "4.1.6--hd175d40_0"
 - "4.1.6--hcb620b3_1"
description: "singularity registry hpc automated addition for minimac4"
config: {"url": "https://biocontainers.pro/tools/minimac4", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for minimac4", "latest": {"4.1.6--hcb620b3_1": "sha256:d5c1e5a5012aa9a0509824e33c31e445b1238d776478a64e016300581c2b4003"}, "tags": {"4.1.6--hd175d40_0": "sha256:acf14632cdc8982bef27e59bc4d88c1d0bd87f1c87c7b665f5be69eb96d08450", "4.1.6--hcb620b3_1": "sha256:d5c1e5a5012aa9a0509824e33c31e445b1238d776478a64e016300581c2b4003"}, "docker": "quay.io/biocontainers/minimac4", "aliases": {"cget": "/usr/local/bin/cget", "edonr256-hash": "/usr/local/bin/edonr256-hash", "edonr512-hash": "/usr/local/bin/edonr512-hash", "gost12-256-hash": "/usr/local/bin/gost12-256-hash", "gost12-512-hash": "/usr/local/bin/gost12-512-hash", "minimac4": "/usr/local/bin/minimac4", "ccmake": "/usr/local/bin/ccmake", "cmake": "/usr/local/bin/cmake", "cpack": "/usr/local/bin/cpack", "ctest": "/usr/local/bin/ctest", "ed2k-link": "/usr/local/bin/ed2k-link", "has160-hash": "/usr/local/bin/has160-hash", "idle3.13": "/usr/local/bin/idle3.13", "magnet-link": "/usr/local/bin/magnet-link", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "rhash": "/usr/local/bin/rhash", "sfv-hash": "/usr/local/bin/sfv-hash", "tiger-hash": "/usr/local/bin/tiger-hash", "tth-hash": "/usr/local/bin/tth-hash", "whirlpool-hash": "/usr/local/bin/whirlpool-hash", "annot-tsv": "/usr/local/bin/annot-tsv", "gff2gff.py": "/usr/local/bin/gff2gff.py", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/minimac4.
singularity registry hpc automated addition for minimac4
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/minimac4
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/minimac4:4.1.6--hcb620b3_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/minimac4/4.1.6--hcb620b3_1
$ module help quay.io/biocontainers/minimac4/4.1.6--hcb620b3_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### minimac4-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### minimac4-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### minimac4-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### minimac4-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### minimac4-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### minimac4-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cget

```bash
$ singularity exec <container> /usr/local/bin/cget
$ podman run --it --rm --entrypoint /usr/local/bin/cget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edonr256-hash

```bash
$ singularity exec <container> /usr/local/bin/edonr256-hash
$ podman run --it --rm --entrypoint /usr/local/bin/edonr256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edonr256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edonr512-hash

```bash
$ singularity exec <container> /usr/local/bin/edonr512-hash
$ podman run --it --rm --entrypoint /usr/local/bin/edonr512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edonr512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gost12-256-hash

```bash
$ singularity exec <container> /usr/local/bin/gost12-256-hash
$ podman run --it --rm --entrypoint /usr/local/bin/gost12-256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gost12-256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gost12-512-hash

```bash
$ singularity exec <container> /usr/local/bin/gost12-512-hash
$ podman run --it --rm --entrypoint /usr/local/bin/gost12-512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gost12-512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimac4

```bash
$ singularity exec <container> /usr/local/bin/minimac4
$ podman run --it --rm --entrypoint /usr/local/bin/minimac4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimac4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccmake

```bash
$ singularity exec <container> /usr/local/bin/ccmake
$ podman run --it --rm --entrypoint /usr/local/bin/ccmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmake

```bash
$ singularity exec <container> /usr/local/bin/cmake
$ podman run --it --rm --entrypoint /usr/local/bin/cmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpack

```bash
$ singularity exec <container> /usr/local/bin/cpack
$ podman run --it --rm --entrypoint /usr/local/bin/cpack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ctest

```bash
$ singularity exec <container> /usr/local/bin/ctest
$ podman run --it --rm --entrypoint /usr/local/bin/ctest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ctest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ed2k-link

```bash
$ singularity exec <container> /usr/local/bin/ed2k-link
$ podman run --it --rm --entrypoint /usr/local/bin/ed2k-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ed2k-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### has160-hash

```bash
$ singularity exec <container> /usr/local/bin/has160-hash
$ podman run --it --rm --entrypoint /usr/local/bin/has160-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/has160-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magnet-link

```bash
$ singularity exec <container> /usr/local/bin/magnet-link
$ podman run --it --rm --entrypoint /usr/local/bin/magnet-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magnet-link   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### rhash

```bash
$ singularity exec <container> /usr/local/bin/rhash
$ podman run --it --rm --entrypoint /usr/local/bin/rhash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rhash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sfv-hash

```bash
$ singularity exec <container> /usr/local/bin/sfv-hash
$ podman run --it --rm --entrypoint /usr/local/bin/sfv-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sfv-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiger-hash

```bash
$ singularity exec <container> /usr/local/bin/tiger-hash
$ podman run --it --rm --entrypoint /usr/local/bin/tiger-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiger-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tth-hash

```bash
$ singularity exec <container> /usr/local/bin/tth-hash
$ podman run --it --rm --entrypoint /usr/local/bin/tth-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tth-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### whirlpool-hash

```bash
$ singularity exec <container> /usr/local/bin/whirlpool-hash
$ podman run --it --rm --entrypoint /usr/local/bin/whirlpool-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/whirlpool-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-vcfstats

```bash
$ singularity exec <container> /usr/local/bin/plot-vcfstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfutils.pl

```bash
$ singularity exec <container> /usr/local/bin/vcfutils.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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