---
layout: container
name:  "quay.io/biocontainers/csuite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/csuite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/csuite/container.yaml"
updated_at: "2026-08-05 05:54:46.109955"
latest: "0.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/csuite"
aliases:
 - "cagecleaner"
 - "cagecleaner-generate-session"
 - "cblaster"
 - "cfoldseeker"
 - "cfoldseeker-cds"
 - "cfoldseeker-seqs"
 - "cidder"
 - "clinker"
 - "csuite"
 - "foldseek"
 - "granet"
 - "kegg_pull"
 - "mgecut"
 - "psghelp"
 - "psgissue"
 - "psgmain"
 - "psgsettings"
 - "psgupgrade"
 - "psgver"
 - "runProdigalAndMakeProperGenbank.py"
 - "skDERcore"
 - "skDERsum"
 - "skani"
 - "skder"
 - "dataformat"
 - "datasets"
 - "gawk-5.4.0"
 - "zless"
 - "fc-genconf"
 - "idna"
 - "pyrodigal"
 - "any2fasta"
 - "archspec"
 - "gunzip"
 - "gzexe"
 - "gzip"
 - "uncompress"
 - "zcat"
 - "zcmp"
 - "zdiff"
 - "zegrep"
 - "zfgrep"
 - "zforce"
 - "zgrep"
 - "zmore"
 - "znew"
 - "funzip"
 - "unzipsfx"
 - "zipgrep"
versions:
 - "0.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for csuite"
config: {"url": "https://biocontainers.pro/tools/csuite", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for csuite", "latest": {"0.1.0--pyhdfd78af_0": "sha256:47b91f03ebd65991d0ad04ebadf227211674289955f4a9d4f170540d4dad8d3c"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:47b91f03ebd65991d0ad04ebadf227211674289955f4a9d4f170540d4dad8d3c"}, "docker": "quay.io/biocontainers/csuite", "aliases": {"cagecleaner": "/usr/local/bin/cagecleaner", "cagecleaner-generate-session": "/usr/local/bin/cagecleaner-generate-session", "cblaster": "/usr/local/bin/cblaster", "cfoldseeker": "/usr/local/bin/cfoldseeker", "cfoldseeker-cds": "/usr/local/bin/cfoldseeker-cds", "cfoldseeker-seqs": "/usr/local/bin/cfoldseeker-seqs", "cidder": "/usr/local/bin/cidder", "clinker": "/usr/local/bin/clinker", "csuite": "/usr/local/bin/csuite", "foldseek": "/usr/local/bin/foldseek", "granet": "/usr/local/bin/granet", "kegg_pull": "/usr/local/bin/kegg_pull", "mgecut": "/usr/local/bin/mgecut", "psghelp": "/usr/local/bin/psghelp", "psgissue": "/usr/local/bin/psgissue", "psgmain": "/usr/local/bin/psgmain", "psgsettings": "/usr/local/bin/psgsettings", "psgupgrade": "/usr/local/bin/psgupgrade", "psgver": "/usr/local/bin/psgver", "runProdigalAndMakeProperGenbank.py": "/usr/local/bin/runProdigalAndMakeProperGenbank.py", "skDERcore": "/usr/local/bin/skDERcore", "skDERsum": "/usr/local/bin/skDERsum", "skani": "/usr/local/bin/skani", "skder": "/usr/local/bin/skder", "dataformat": "/usr/local/bin/dataformat", "datasets": "/usr/local/bin/datasets", "gawk-5.4.0": "/usr/local/bin/gawk-5.4.0", "zless": "/usr/local/bin/zless", "fc-genconf": "/usr/local/bin/fc-genconf", "idna": "/usr/local/bin/idna", "pyrodigal": "/usr/local/bin/pyrodigal", "any2fasta": "/usr/local/bin/any2fasta", "archspec": "/usr/local/bin/archspec", "gunzip": "/usr/local/bin/gunzip", "gzexe": "/usr/local/bin/gzexe", "gzip": "/usr/local/bin/gzip", "uncompress": "/usr/local/bin/uncompress", "zcat": "/usr/local/bin/zcat", "zcmp": "/usr/local/bin/zcmp", "zdiff": "/usr/local/bin/zdiff", "zegrep": "/usr/local/bin/zegrep", "zfgrep": "/usr/local/bin/zfgrep", "zforce": "/usr/local/bin/zforce", "zgrep": "/usr/local/bin/zgrep", "zmore": "/usr/local/bin/zmore", "znew": "/usr/local/bin/znew", "funzip": "/usr/local/bin/funzip", "unzipsfx": "/usr/local/bin/unzipsfx", "zipgrep": "/usr/local/bin/zipgrep"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/csuite.
singularity registry hpc automated addition for csuite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/csuite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/csuite:0.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/csuite/0.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/csuite/0.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### csuite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### csuite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### csuite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### csuite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### csuite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### csuite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cagecleaner

```bash
$ singularity exec <container> /usr/local/bin/cagecleaner
$ podman run --it --rm --entrypoint /usr/local/bin/cagecleaner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cagecleaner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cagecleaner-generate-session

```bash
$ singularity exec <container> /usr/local/bin/cagecleaner-generate-session
$ podman run --it --rm --entrypoint /usr/local/bin/cagecleaner-generate-session   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cagecleaner-generate-session   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cblaster

```bash
$ singularity exec <container> /usr/local/bin/cblaster
$ podman run --it --rm --entrypoint /usr/local/bin/cblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cfoldseeker

```bash
$ singularity exec <container> /usr/local/bin/cfoldseeker
$ podman run --it --rm --entrypoint /usr/local/bin/cfoldseeker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cfoldseeker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cfoldseeker-cds

```bash
$ singularity exec <container> /usr/local/bin/cfoldseeker-cds
$ podman run --it --rm --entrypoint /usr/local/bin/cfoldseeker-cds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cfoldseeker-cds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cfoldseeker-seqs

```bash
$ singularity exec <container> /usr/local/bin/cfoldseeker-seqs
$ podman run --it --rm --entrypoint /usr/local/bin/cfoldseeker-seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cfoldseeker-seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cidder

```bash
$ singularity exec <container> /usr/local/bin/cidder
$ podman run --it --rm --entrypoint /usr/local/bin/cidder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cidder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clinker

```bash
$ singularity exec <container> /usr/local/bin/clinker
$ podman run --it --rm --entrypoint /usr/local/bin/clinker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clinker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csuite

```bash
$ singularity exec <container> /usr/local/bin/csuite
$ podman run --it --rm --entrypoint /usr/local/bin/csuite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csuite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### foldseek

```bash
$ singularity exec <container> /usr/local/bin/foldseek
$ podman run --it --rm --entrypoint /usr/local/bin/foldseek   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/foldseek   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### granet

```bash
$ singularity exec <container> /usr/local/bin/granet
$ podman run --it --rm --entrypoint /usr/local/bin/granet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/granet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kegg_pull

```bash
$ singularity exec <container> /usr/local/bin/kegg_pull
$ podman run --it --rm --entrypoint /usr/local/bin/kegg_pull   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kegg_pull   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mgecut

```bash
$ singularity exec <container> /usr/local/bin/mgecut
$ podman run --it --rm --entrypoint /usr/local/bin/mgecut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mgecut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psghelp

```bash
$ singularity exec <container> /usr/local/bin/psghelp
$ podman run --it --rm --entrypoint /usr/local/bin/psghelp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psghelp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psgissue

```bash
$ singularity exec <container> /usr/local/bin/psgissue
$ podman run --it --rm --entrypoint /usr/local/bin/psgissue   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psgissue   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psgmain

```bash
$ singularity exec <container> /usr/local/bin/psgmain
$ podman run --it --rm --entrypoint /usr/local/bin/psgmain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psgmain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psgsettings

```bash
$ singularity exec <container> /usr/local/bin/psgsettings
$ podman run --it --rm --entrypoint /usr/local/bin/psgsettings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psgsettings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psgupgrade

```bash
$ singularity exec <container> /usr/local/bin/psgupgrade
$ podman run --it --rm --entrypoint /usr/local/bin/psgupgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psgupgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psgver

```bash
$ singularity exec <container> /usr/local/bin/psgver
$ podman run --it --rm --entrypoint /usr/local/bin/psgver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psgver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runProdigalAndMakeProperGenbank.py

```bash
$ singularity exec <container> /usr/local/bin/runProdigalAndMakeProperGenbank.py
$ podman run --it --rm --entrypoint /usr/local/bin/runProdigalAndMakeProperGenbank.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runProdigalAndMakeProperGenbank.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skDERcore

```bash
$ singularity exec <container> /usr/local/bin/skDERcore
$ podman run --it --rm --entrypoint /usr/local/bin/skDERcore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skDERcore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skDERsum

```bash
$ singularity exec <container> /usr/local/bin/skDERsum
$ podman run --it --rm --entrypoint /usr/local/bin/skDERsum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skDERsum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skani

```bash
$ singularity exec <container> /usr/local/bin/skani
$ podman run --it --rm --entrypoint /usr/local/bin/skani   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skani   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skder

```bash
$ singularity exec <container> /usr/local/bin/skder
$ podman run --it --rm --entrypoint /usr/local/bin/skder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dataformat

```bash
$ singularity exec <container> /usr/local/bin/dataformat
$ podman run --it --rm --entrypoint /usr/local/bin/dataformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dataformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### datasets

```bash
$ singularity exec <container> /usr/local/bin/datasets
$ podman run --it --rm --entrypoint /usr/local/bin/datasets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datasets   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### zfgrep

```bash
$ singularity exec <container> /usr/local/bin/zfgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zforce

```bash
$ singularity exec <container> /usr/local/bin/zforce
$ podman run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zgrep

```bash
$ singularity exec <container> /usr/local/bin/zgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zmore

```bash
$ singularity exec <container> /usr/local/bin/zmore
$ podman run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### znew

```bash
$ singularity exec <container> /usr/local/bin/znew
$ podman run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### funzip

```bash
$ singularity exec <container> /usr/local/bin/funzip
$ podman run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzipsfx

```bash
$ singularity exec <container> /usr/local/bin/unzipsfx
$ podman run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipgrep

```bash
$ singularity exec <container> /usr/local/bin/zipgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
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