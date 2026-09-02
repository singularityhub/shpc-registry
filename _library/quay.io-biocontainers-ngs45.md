---
layout: container
name:  "quay.io/biocontainers/ngs45"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngs45/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ngs45/container.yaml"
updated_at: "2026-09-02 07:12:27.231956"
latest: "0.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/ngs45"
aliases:
 - "2ndscore"
 - "ITSx"
 - "binspreader"
 - "calibrate.sh"
 - "make_expterm.py"
 - "mfold_rna.sh"
 - "ngs45"
 - "pathracer-seq-fs"
 - "psl"
 - "psl-make-dafsa"
 - "random_fasta.py"
 - "spades-hpc"
 - "transterm"
 - "ziggypep"
 - "pathracer"
 - "spades-gfa-split"
 - "taxonkit"
 - "gff2gff"
 - "roh-viz"
 - "vrfs-variances"
 - "gawk-5.4.0"
 - "zless"
 - "coronaspades.py"
 - "metaplasmidspades.py"
 - "metaviralspades.py"
 - "rnaviralspades.py"
 - "splitter"
 - "pyrodigal"
 - "any2fasta"
 - "archspec"
 - "barrnap"
 - "gunzip"
 - "gzexe"
 - "gzip"
 - "uncompress"
 - "zcat"
 - "zcmp"
 - "zdiff"
 - "zegrep"
versions:
 - "0.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for ngs45"
config: {"url": "https://biocontainers.pro/tools/ngs45", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ngs45", "latest": {"0.1.0--pyhdfd78af_0": "sha256:326fd404d3871d5b0487d9c8485c0644a5d6150778f8f8d7efa4873ab35234d4"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:326fd404d3871d5b0487d9c8485c0644a5d6150778f8f8d7efa4873ab35234d4"}, "docker": "quay.io/biocontainers/ngs45", "aliases": {"2ndscore": "/usr/local/bin/2ndscore", "ITSx": "/usr/local/bin/ITSx", "binspreader": "/usr/local/bin/binspreader", "calibrate.sh": "/usr/local/bin/calibrate.sh", "make_expterm.py": "/usr/local/bin/make_expterm.py", "mfold_rna.sh": "/usr/local/bin/mfold_rna.sh", "ngs45": "/usr/local/bin/ngs45", "pathracer-seq-fs": "/usr/local/bin/pathracer-seq-fs", "psl": "/usr/local/bin/psl", "psl-make-dafsa": "/usr/local/bin/psl-make-dafsa", "random_fasta.py": "/usr/local/bin/random_fasta.py", "spades-hpc": "/usr/local/bin/spades-hpc", "transterm": "/usr/local/bin/transterm", "ziggypep": "/usr/local/bin/ziggypep", "pathracer": "/usr/local/bin/pathracer", "spades-gfa-split": "/usr/local/bin/spades-gfa-split", "taxonkit": "/usr/local/bin/taxonkit", "gff2gff": "/usr/local/bin/gff2gff", "roh-viz": "/usr/local/bin/roh-viz", "vrfs-variances": "/usr/local/bin/vrfs-variances", "gawk-5.4.0": "/usr/local/bin/gawk-5.4.0", "zless": "/usr/local/bin/zless", "coronaspades.py": "/usr/local/bin/coronaspades.py", "metaplasmidspades.py": "/usr/local/bin/metaplasmidspades.py", "metaviralspades.py": "/usr/local/bin/metaviralspades.py", "rnaviralspades.py": "/usr/local/bin/rnaviralspades.py", "splitter": "/usr/local/bin/splitter", "pyrodigal": "/usr/local/bin/pyrodigal", "any2fasta": "/usr/local/bin/any2fasta", "archspec": "/usr/local/bin/archspec", "barrnap": "/usr/local/bin/barrnap", "gunzip": "/usr/local/bin/gunzip", "gzexe": "/usr/local/bin/gzexe", "gzip": "/usr/local/bin/gzip", "uncompress": "/usr/local/bin/uncompress", "zcat": "/usr/local/bin/zcat", "zcmp": "/usr/local/bin/zcmp", "zdiff": "/usr/local/bin/zdiff", "zegrep": "/usr/local/bin/zegrep"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ngs45.
singularity registry hpc automated addition for ngs45
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ngs45
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ngs45:0.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ngs45/0.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/ngs45/0.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ngs45-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ngs45-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ngs45-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ngs45-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ngs45-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ngs45-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2ndscore

```bash
$ singularity exec <container> /usr/local/bin/2ndscore
$ podman run --it --rm --entrypoint /usr/local/bin/2ndscore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2ndscore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ITSx

```bash
$ singularity exec <container> /usr/local/bin/ITSx
$ podman run --it --rm --entrypoint /usr/local/bin/ITSx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ITSx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### binspreader

```bash
$ singularity exec <container> /usr/local/bin/binspreader
$ podman run --it --rm --entrypoint /usr/local/bin/binspreader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binspreader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calibrate.sh

```bash
$ singularity exec <container> /usr/local/bin/calibrate.sh
$ podman run --it --rm --entrypoint /usr/local/bin/calibrate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calibrate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_expterm.py

```bash
$ singularity exec <container> /usr/local/bin/make_expterm.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_expterm.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_expterm.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mfold_rna.sh

```bash
$ singularity exec <container> /usr/local/bin/mfold_rna.sh
$ podman run --it --rm --entrypoint /usr/local/bin/mfold_rna.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mfold_rna.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngs45

```bash
$ singularity exec <container> /usr/local/bin/ngs45
$ podman run --it --rm --entrypoint /usr/local/bin/ngs45   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngs45   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathracer-seq-fs

```bash
$ singularity exec <container> /usr/local/bin/pathracer-seq-fs
$ podman run --it --rm --entrypoint /usr/local/bin/pathracer-seq-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathracer-seq-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl

```bash
$ singularity exec <container> /usr/local/bin/psl
$ podman run --it --rm --entrypoint /usr/local/bin/psl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl-make-dafsa

```bash
$ singularity exec <container> /usr/local/bin/psl-make-dafsa
$ podman run --it --rm --entrypoint /usr/local/bin/psl-make-dafsa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl-make-dafsa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### random_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/random_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/random_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/random_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-hpc

```bash
$ singularity exec <container> /usr/local/bin/spades-hpc
$ podman run --it --rm --entrypoint /usr/local/bin/spades-hpc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-hpc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transterm

```bash
$ singularity exec <container> /usr/local/bin/transterm
$ podman run --it --rm --entrypoint /usr/local/bin/transterm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transterm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ziggypep

```bash
$ singularity exec <container> /usr/local/bin/ziggypep
$ podman run --it --rm --entrypoint /usr/local/bin/ziggypep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ziggypep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathracer

```bash
$ singularity exec <container> /usr/local/bin/pathracer
$ podman run --it --rm --entrypoint /usr/local/bin/pathracer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathracer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gfa-split

```bash
$ singularity exec <container> /usr/local/bin/spades-gfa-split
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gfa-split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gfa-split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxonkit

```bash
$ singularity exec <container> /usr/local/bin/taxonkit
$ podman run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff

```bash
$ singularity exec <container> /usr/local/bin/gff2gff
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roh-viz

```bash
$ singularity exec <container> /usr/local/bin/roh-viz
$ podman run --it --rm --entrypoint /usr/local/bin/roh-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roh-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vrfs-variances

```bash
$ singularity exec <container> /usr/local/bin/vrfs-variances
$ podman run --it --rm --entrypoint /usr/local/bin/vrfs-variances   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vrfs-variances   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.4.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.4.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zless

```bash
$ singularity exec <container> /usr/local/bin/zless
$ podman run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coronaspades.py

```bash
$ singularity exec <container> /usr/local/bin/coronaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaplasmidspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaplasmidspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaplasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaplasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaviralspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaviralspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaviralspades.py

```bash
$ singularity exec <container> /usr/local/bin/rnaviralspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitter

```bash
$ singularity exec <container> /usr/local/bin/splitter
$ podman run --it --rm --entrypoint /usr/local/bin/splitter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrodigal

```bash
$ singularity exec <container> /usr/local/bin/pyrodigal
$ podman run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### any2fasta

```bash
$ singularity exec <container> /usr/local/bin/any2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archspec

```bash
$ singularity exec <container> /usr/local/bin/archspec
$ podman run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### barrnap

```bash
$ singularity exec <container> /usr/local/bin/barrnap
$ podman run --it --rm --entrypoint /usr/local/bin/barrnap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/barrnap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gunzip

```bash
$ singularity exec <container> /usr/local/bin/gunzip
$ podman run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzexe

```bash
$ singularity exec <container> /usr/local/bin/gzexe
$ podman run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzip

```bash
$ singularity exec <container> /usr/local/bin/gzip
$ podman run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uncompress

```bash
$ singularity exec <container> /usr/local/bin/uncompress
$ podman run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcat

```bash
$ singularity exec <container> /usr/local/bin/zcat
$ podman run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcmp

```bash
$ singularity exec <container> /usr/local/bin/zcmp
$ podman run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zdiff

```bash
$ singularity exec <container> /usr/local/bin/zdiff
$ podman run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zegrep

```bash
$ singularity exec <container> /usr/local/bin/zegrep
$ podman run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
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