---
layout: container
name:  "quay.io/biocontainers/milonga"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/milonga/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/milonga/container.yaml"
updated_at: "2024-03-05 02:59:08.515761"
latest: "1.0.3--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/milonga"
aliases:
 - "NanoFilt"
 - "NanoStat"
 - "TMalign"
 - "abricate"
 - "abricate-get_db"
 - "bioawk"
 - "checkm"
 - "coronaspades.py"
 - "create_hybrid_samplesheet.sh"
 - "make_pscores.pl"
 - "metaplasmidspades.py"
 - "metaviralspades.py"
 - "milonga.py"
 - "milonga_setup.sh"
 - "platon"
 - "qcat"
 - "qcat-eval"
 - "qcat-eval-truth"
 - "qcat-roc"
 - "rnaviralspades.py"
 - "taxonkit"
 - "unicycler"
 - "kraken2"
 - "kraken2-build"
 - "kraken2-inspect"
 - "poa"
 - "porechop"
 - "miniasm"
 - "minidot"
 - "flye-modules"
 - "flye-samtools"
 - "delta2vcf"
 - "flye"
 - "flye-minimap2"
 - "pilon"
 - "rppr"
 - "RNAmultifold"
 - "rsync-ssl"
 - "clustalo"
 - "guppy"
 - "pplacer"
 - "any2fasta"
 - "hwloc-gather-cpuid"
 - "rsync"
 - "hwloc-annotate"
 - "hwloc-bind"
 - "hwloc-calc"
versions:
 - "1.0.1--hdfd78af_0"
 - "1.0.3--hdfd78af_0"
description: "singularity registry hpc automated addition for milonga"
config: {"url": "https://biocontainers.pro/tools/milonga", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for milonga", "latest": {"1.0.3--hdfd78af_0": "sha256:267ed3f8c56119f6fe5d3c343bbf685871a5a55e443e964f96d8b5161c611208"}, "tags": {"1.0.1--hdfd78af_0": "sha256:31429d69e7eb1ad062275898918ba50f4d3af087bd3c099b85c2823928ee70c4", "1.0.3--hdfd78af_0": "sha256:267ed3f8c56119f6fe5d3c343bbf685871a5a55e443e964f96d8b5161c611208"}, "docker": "quay.io/biocontainers/milonga", "aliases": {"NanoFilt": "/usr/local/bin/NanoFilt", "NanoStat": "/usr/local/bin/NanoStat", "TMalign": "/usr/local/bin/TMalign", "abricate": "/usr/local/bin/abricate", "abricate-get_db": "/usr/local/bin/abricate-get_db", "bioawk": "/usr/local/bin/bioawk", "checkm": "/usr/local/bin/checkm", "coronaspades.py": "/usr/local/bin/coronaspades.py", "create_hybrid_samplesheet.sh": "/usr/local/bin/create_hybrid_samplesheet.sh", "make_pscores.pl": "/usr/local/bin/make_pscores.pl", "metaplasmidspades.py": "/usr/local/bin/metaplasmidspades.py", "metaviralspades.py": "/usr/local/bin/metaviralspades.py", "milonga.py": "/usr/local/bin/milonga.py", "milonga_setup.sh": "/usr/local/bin/milonga_setup.sh", "platon": "/usr/local/bin/platon", "qcat": "/usr/local/bin/qcat", "qcat-eval": "/usr/local/bin/qcat-eval", "qcat-eval-truth": "/usr/local/bin/qcat-eval-truth", "qcat-roc": "/usr/local/bin/qcat-roc", "rnaviralspades.py": "/usr/local/bin/rnaviralspades.py", "taxonkit": "/usr/local/bin/taxonkit", "unicycler": "/usr/local/bin/unicycler", "kraken2": "/usr/local/bin/kraken2", "kraken2-build": "/usr/local/bin/kraken2-build", "kraken2-inspect": "/usr/local/bin/kraken2-inspect", "poa": "/usr/local/bin/poa", "porechop": "/usr/local/bin/porechop", "miniasm": "/usr/local/bin/miniasm", "minidot": "/usr/local/bin/minidot", "flye-modules": "/usr/local/bin/flye-modules", "flye-samtools": "/usr/local/bin/flye-samtools", "delta2vcf": "/usr/local/bin/delta2vcf", "flye": "/usr/local/bin/flye", "flye-minimap2": "/usr/local/bin/flye-minimap2", "pilon": "/usr/local/bin/pilon", "rppr": "/usr/local/bin/rppr", "RNAmultifold": "/usr/local/bin/RNAmultifold", "rsync-ssl": "/usr/local/bin/rsync-ssl", "clustalo": "/usr/local/bin/clustalo", "guppy": "/usr/local/bin/guppy", "pplacer": "/usr/local/bin/pplacer", "any2fasta": "/usr/local/bin/any2fasta", "hwloc-gather-cpuid": "/usr/local/bin/hwloc-gather-cpuid", "rsync": "/usr/local/bin/rsync", "hwloc-annotate": "/usr/local/bin/hwloc-annotate", "hwloc-bind": "/usr/local/bin/hwloc-bind", "hwloc-calc": "/usr/local/bin/hwloc-calc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/milonga.
singularity registry hpc automated addition for milonga
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/milonga
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/milonga:1.0.3--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/milonga/1.0.3--hdfd78af_0
$ module help quay.io/biocontainers/milonga/1.0.3--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### milonga-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### milonga-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### milonga-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### milonga-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### milonga-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### milonga-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NanoFilt

```bash
$ singularity exec <container> /usr/local/bin/NanoFilt
$ podman run --it --rm --entrypoint /usr/local/bin/NanoFilt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NanoFilt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### NanoStat

```bash
$ singularity exec <container> /usr/local/bin/NanoStat
$ podman run --it --rm --entrypoint /usr/local/bin/NanoStat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NanoStat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TMalign

```bash
$ singularity exec <container> /usr/local/bin/TMalign
$ podman run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abricate

```bash
$ singularity exec <container> /usr/local/bin/abricate
$ podman run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abricate-get_db

```bash
$ singularity exec <container> /usr/local/bin/abricate-get_db
$ podman run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bioawk

```bash
$ singularity exec <container> /usr/local/bin/bioawk
$ podman run --it --rm --entrypoint /usr/local/bin/bioawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkm

```bash
$ singularity exec <container> /usr/local/bin/checkm
$ podman run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coronaspades.py

```bash
$ singularity exec <container> /usr/local/bin/coronaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_hybrid_samplesheet.sh

```bash
$ singularity exec <container> /usr/local/bin/create_hybrid_samplesheet.sh
$ podman run --it --rm --entrypoint /usr/local/bin/create_hybrid_samplesheet.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_hybrid_samplesheet.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_pscores.pl

```bash
$ singularity exec <container> /usr/local/bin/make_pscores.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_pscores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_pscores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### milonga.py

```bash
$ singularity exec <container> /usr/local/bin/milonga.py
$ podman run --it --rm --entrypoint /usr/local/bin/milonga.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/milonga.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### milonga_setup.sh

```bash
$ singularity exec <container> /usr/local/bin/milonga_setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/milonga_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/milonga_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### platon

```bash
$ singularity exec <container> /usr/local/bin/platon
$ podman run --it --rm --entrypoint /usr/local/bin/platon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/platon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qcat

```bash
$ singularity exec <container> /usr/local/bin/qcat
$ podman run --it --rm --entrypoint /usr/local/bin/qcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qcat-eval

```bash
$ singularity exec <container> /usr/local/bin/qcat-eval
$ podman run --it --rm --entrypoint /usr/local/bin/qcat-eval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qcat-eval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qcat-eval-truth

```bash
$ singularity exec <container> /usr/local/bin/qcat-eval-truth
$ podman run --it --rm --entrypoint /usr/local/bin/qcat-eval-truth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qcat-eval-truth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qcat-roc

```bash
$ singularity exec <container> /usr/local/bin/qcat-roc
$ podman run --it --rm --entrypoint /usr/local/bin/qcat-roc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qcat-roc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaviralspades.py

```bash
$ singularity exec <container> /usr/local/bin/rnaviralspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxonkit

```bash
$ singularity exec <container> /usr/local/bin/taxonkit
$ podman run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unicycler

```bash
$ singularity exec <container> /usr/local/bin/unicycler
$ podman run --it --rm --entrypoint /usr/local/bin/unicycler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unicycler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2

```bash
$ singularity exec <container> /usr/local/bin/kraken2
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2-build

```bash
$ singularity exec <container> /usr/local/bin/kraken2-build
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2-inspect

```bash
$ singularity exec <container> /usr/local/bin/kraken2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### poa

```bash
$ singularity exec <container> /usr/local/bin/poa
$ podman run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### porechop

```bash
$ singularity exec <container> /usr/local/bin/porechop
$ podman run --it --rm --entrypoint /usr/local/bin/porechop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/porechop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miniasm

```bash
$ singularity exec <container> /usr/local/bin/miniasm
$ podman run --it --rm --entrypoint /usr/local/bin/miniasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miniasm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minidot

```bash
$ singularity exec <container> /usr/local/bin/minidot
$ podman run --it --rm --entrypoint /usr/local/bin/minidot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minidot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-modules

```bash
$ singularity exec <container> /usr/local/bin/flye-modules
$ podman run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-samtools

```bash
$ singularity exec <container> /usr/local/bin/flye-samtools
$ podman run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta2vcf

```bash
$ singularity exec <container> /usr/local/bin/delta2vcf
$ podman run --it --rm --entrypoint /usr/local/bin/delta2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye

```bash
$ singularity exec <container> /usr/local/bin/flye
$ podman run --it --rm --entrypoint /usr/local/bin/flye   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-minimap2

```bash
$ singularity exec <container> /usr/local/bin/flye-minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/flye-minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilon

```bash
$ singularity exec <container> /usr/local/bin/pilon
$ podman run --it --rm --entrypoint /usr/local/bin/pilon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rppr

```bash
$ singularity exec <container> /usr/local/bin/rppr
$ podman run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAmultifold

```bash
$ singularity exec <container> /usr/local/bin/RNAmultifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsync-ssl

```bash
$ singularity exec <container> /usr/local/bin/rsync-ssl
$ podman run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalo

```bash
$ singularity exec <container> /usr/local/bin/clustalo
$ podman run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guppy

```bash
$ singularity exec <container> /usr/local/bin/guppy
$ podman run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pplacer

```bash
$ singularity exec <container> /usr/local/bin/pplacer
$ podman run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### any2fasta

```bash
$ singularity exec <container> /usr/local/bin/any2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-gather-cpuid

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-cpuid
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsync

```bash
$ singularity exec <container> /usr/local/bin/rsync
$ podman run --it --rm --entrypoint /usr/local/bin/rsync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsync   -v ${PWD} -w ${PWD} <container> -c " $@"
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