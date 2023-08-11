---
layout: container
name:  "quay.io/biocontainers/aquamis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aquamis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/aquamis/container.yaml"
updated_at: "2023-08-11 02:31:42.724377"
latest: "1.3.7--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/aquamis"
aliases:
 - "aquamis"
 - "aquamis_setup.sh"
 - "bracken"
 - "bracken-build"
 - "combine_bracken_outputs.py"
 - "confindr"
 - "confindr.py"
 - "confindr_create_db"
 - "confindr_database_setup"
 - "create_sampleSheet.sh"
 - "est_abundance.py"
 - "filter_json.py"
 - "generate_kmer_distribution.py"
 - "genson"
 - "helper_functions.py"
 - "icarus.py"
 - "kma"
 - "kma_index"
 - "kma_shm"
 - "kma_update"
 - "kmer2read_distr"
 - "kraken2"
 - "kraken2-build"
 - "kraken2-inspect"
 - "lighter"
 - "metaquast"
 - "metaquast.py"
 - "mlst"
 - "parse_json.py"
 - "quast"
 - "quast-download-busco"
 - "quast-download-gridss"
 - "quast-download-silva"
 - "quast-lg.py"
 - "quast.py"
 - "shovill"
 - "skesa"
 - "taxonkit"
 - "write_QC_report.Rmd"
 - "write_report.Rmd"
 - "kmutate.sh"
 - "megahit_core"
 - "megahit_core_no_hw_accel"
 - "megahit_core_popcnt"
 - "rsync-ssl"
 - "runhmm.sh"
 - "circos"
 - "circos.exe"
 - "compile.bat"
 - "compile.make"
versions:
 - "1.3.7--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for aquamis"
config: {"url": "https://biocontainers.pro/tools/aquamis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for aquamis", "latest": {"1.3.7--hdfd78af_0": "sha256:f40422049c5ebde54311e8e75d4ac931ecf07bcd218cf8c7abffe21aaf8d151e"}, "tags": {"1.3.7--hdfd78af_0": "sha256:f40422049c5ebde54311e8e75d4ac931ecf07bcd218cf8c7abffe21aaf8d151e"}, "docker": "quay.io/biocontainers/aquamis", "aliases": {"aquamis": "/usr/local/bin/aquamis", "aquamis_setup.sh": "/usr/local/bin/aquamis_setup.sh", "bracken": "/usr/local/bin/bracken", "bracken-build": "/usr/local/bin/bracken-build", "combine_bracken_outputs.py": "/usr/local/bin/combine_bracken_outputs.py", "confindr": "/usr/local/bin/confindr", "confindr.py": "/usr/local/bin/confindr.py", "confindr_create_db": "/usr/local/bin/confindr_create_db", "confindr_database_setup": "/usr/local/bin/confindr_database_setup", "create_sampleSheet.sh": "/usr/local/bin/create_sampleSheet.sh", "est_abundance.py": "/usr/local/bin/est_abundance.py", "filter_json.py": "/usr/local/bin/filter_json.py", "generate_kmer_distribution.py": "/usr/local/bin/generate_kmer_distribution.py", "genson": "/usr/local/bin/genson", "helper_functions.py": "/usr/local/bin/helper_functions.py", "icarus.py": "/usr/local/bin/icarus.py", "kma": "/usr/local/bin/kma", "kma_index": "/usr/local/bin/kma_index", "kma_shm": "/usr/local/bin/kma_shm", "kma_update": "/usr/local/bin/kma_update", "kmer2read_distr": "/usr/local/bin/kmer2read_distr", "kraken2": "/usr/local/bin/kraken2", "kraken2-build": "/usr/local/bin/kraken2-build", "kraken2-inspect": "/usr/local/bin/kraken2-inspect", "lighter": "/usr/local/bin/lighter", "metaquast": "/usr/local/bin/metaquast", "metaquast.py": "/usr/local/bin/metaquast.py", "mlst": "/usr/local/bin/mlst", "parse_json.py": "/usr/local/bin/parse_json.py", "quast": "/usr/local/bin/quast", "quast-download-busco": "/usr/local/bin/quast-download-busco", "quast-download-gridss": "/usr/local/bin/quast-download-gridss", "quast-download-silva": "/usr/local/bin/quast-download-silva", "quast-lg.py": "/usr/local/bin/quast-lg.py", "quast.py": "/usr/local/bin/quast.py", "shovill": "/usr/local/bin/shovill", "skesa": "/usr/local/bin/skesa", "taxonkit": "/usr/local/bin/taxonkit", "write_QC_report.Rmd": "/usr/local/bin/write_QC_report.Rmd", "write_report.Rmd": "/usr/local/bin/write_report.Rmd", "kmutate.sh": "/usr/local/bin/kmutate.sh", "megahit_core": "/usr/local/bin/megahit_core", "megahit_core_no_hw_accel": "/usr/local/bin/megahit_core_no_hw_accel", "megahit_core_popcnt": "/usr/local/bin/megahit_core_popcnt", "rsync-ssl": "/usr/local/bin/rsync-ssl", "runhmm.sh": "/usr/local/bin/runhmm.sh", "circos": "/usr/local/bin/circos", "circos.exe": "/usr/local/bin/circos.exe", "compile.bat": "/usr/local/bin/compile.bat", "compile.make": "/usr/local/bin/compile.make"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aquamis.
shpc-registry automated BioContainers addition for aquamis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aquamis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aquamis:1.3.7--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aquamis/1.3.7--hdfd78af_0
$ module help quay.io/biocontainers/aquamis/1.3.7--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aquamis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aquamis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aquamis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aquamis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aquamis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aquamis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aquamis

```bash
$ singularity exec <container> /usr/local/bin/aquamis
$ podman run --it --rm --entrypoint /usr/local/bin/aquamis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aquamis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aquamis_setup.sh

```bash
$ singularity exec <container> /usr/local/bin/aquamis_setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/aquamis_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aquamis_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bracken

```bash
$ singularity exec <container> /usr/local/bin/bracken
$ podman run --it --rm --entrypoint /usr/local/bin/bracken   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bracken   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bracken-build

```bash
$ singularity exec <container> /usr/local/bin/bracken-build
$ podman run --it --rm --entrypoint /usr/local/bin/bracken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bracken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_bracken_outputs.py

```bash
$ singularity exec <container> /usr/local/bin/combine_bracken_outputs.py
$ podman run --it --rm --entrypoint /usr/local/bin/combine_bracken_outputs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_bracken_outputs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### confindr

```bash
$ singularity exec <container> /usr/local/bin/confindr
$ podman run --it --rm --entrypoint /usr/local/bin/confindr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/confindr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### confindr.py

```bash
$ singularity exec <container> /usr/local/bin/confindr.py
$ podman run --it --rm --entrypoint /usr/local/bin/confindr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/confindr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### confindr_create_db

```bash
$ singularity exec <container> /usr/local/bin/confindr_create_db
$ podman run --it --rm --entrypoint /usr/local/bin/confindr_create_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/confindr_create_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### confindr_database_setup

```bash
$ singularity exec <container> /usr/local/bin/confindr_database_setup
$ podman run --it --rm --entrypoint /usr/local/bin/confindr_database_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/confindr_database_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_sampleSheet.sh

```bash
$ singularity exec <container> /usr/local/bin/create_sampleSheet.sh
$ podman run --it --rm --entrypoint /usr/local/bin/create_sampleSheet.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_sampleSheet.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### est_abundance.py

```bash
$ singularity exec <container> /usr/local/bin/est_abundance.py
$ podman run --it --rm --entrypoint /usr/local/bin/est_abundance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/est_abundance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_json.py

```bash
$ singularity exec <container> /usr/local/bin/filter_json.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_json.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_json.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_kmer_distribution.py

```bash
$ singularity exec <container> /usr/local/bin/generate_kmer_distribution.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_kmer_distribution.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_kmer_distribution.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genson

```bash
$ singularity exec <container> /usr/local/bin/genson
$ podman run --it --rm --entrypoint /usr/local/bin/genson   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genson   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### helper_functions.py

```bash
$ singularity exec <container> /usr/local/bin/helper_functions.py
$ podman run --it --rm --entrypoint /usr/local/bin/helper_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/helper_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### icarus.py

```bash
$ singularity exec <container> /usr/local/bin/icarus.py
$ podman run --it --rm --entrypoint /usr/local/bin/icarus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/icarus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma

```bash
$ singularity exec <container> /usr/local/bin/kma
$ podman run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_index

```bash
$ singularity exec <container> /usr/local/bin/kma_index
$ podman run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_shm

```bash
$ singularity exec <container> /usr/local/bin/kma_shm
$ podman run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_update

```bash
$ singularity exec <container> /usr/local/bin/kma_update
$ podman run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmer2read_distr

```bash
$ singularity exec <container> /usr/local/bin/kmer2read_distr
$ podman run --it --rm --entrypoint /usr/local/bin/kmer2read_distr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer2read_distr   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### lighter

```bash
$ singularity exec <container> /usr/local/bin/lighter
$ podman run --it --rm --entrypoint /usr/local/bin/lighter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lighter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaquast

```bash
$ singularity exec <container> /usr/local/bin/metaquast
$ podman run --it --rm --entrypoint /usr/local/bin/metaquast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaquast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaquast.py

```bash
$ singularity exec <container> /usr/local/bin/metaquast.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaquast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaquast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlst

```bash
$ singularity exec <container> /usr/local/bin/mlst
$ podman run --it --rm --entrypoint /usr/local/bin/mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parse_json.py

```bash
$ singularity exec <container> /usr/local/bin/parse_json.py
$ podman run --it --rm --entrypoint /usr/local/bin/parse_json.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parse_json.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast

```bash
$ singularity exec <container> /usr/local/bin/quast
$ podman run --it --rm --entrypoint /usr/local/bin/quast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast-download-busco

```bash
$ singularity exec <container> /usr/local/bin/quast-download-busco
$ podman run --it --rm --entrypoint /usr/local/bin/quast-download-busco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast-download-busco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast-download-gridss

```bash
$ singularity exec <container> /usr/local/bin/quast-download-gridss
$ podman run --it --rm --entrypoint /usr/local/bin/quast-download-gridss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast-download-gridss   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast-download-silva

```bash
$ singularity exec <container> /usr/local/bin/quast-download-silva
$ podman run --it --rm --entrypoint /usr/local/bin/quast-download-silva   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast-download-silva   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast-lg.py

```bash
$ singularity exec <container> /usr/local/bin/quast-lg.py
$ podman run --it --rm --entrypoint /usr/local/bin/quast-lg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast-lg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast.py

```bash
$ singularity exec <container> /usr/local/bin/quast.py
$ podman run --it --rm --entrypoint /usr/local/bin/quast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shovill

```bash
$ singularity exec <container> /usr/local/bin/shovill
$ podman run --it --rm --entrypoint /usr/local/bin/shovill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shovill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skesa

```bash
$ singularity exec <container> /usr/local/bin/skesa
$ podman run --it --rm --entrypoint /usr/local/bin/skesa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skesa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxonkit

```bash
$ singularity exec <container> /usr/local/bin/taxonkit
$ podman run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### write_QC_report.Rmd

```bash
$ singularity exec <container> /usr/local/bin/write_QC_report.Rmd
$ podman run --it --rm --entrypoint /usr/local/bin/write_QC_report.Rmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/write_QC_report.Rmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### write_report.Rmd

```bash
$ singularity exec <container> /usr/local/bin/write_report.Rmd
$ podman run --it --rm --entrypoint /usr/local/bin/write_report.Rmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/write_report.Rmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmutate.sh

```bash
$ singularity exec <container> /usr/local/bin/kmutate.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core

```bash
$ singularity exec <container> /usr/local/bin/megahit_core
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core_no_hw_accel

```bash
$ singularity exec <container> /usr/local/bin/megahit_core_no_hw_accel
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core_no_hw_accel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core_no_hw_accel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core_popcnt

```bash
$ singularity exec <container> /usr/local/bin/megahit_core_popcnt
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core_popcnt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core_popcnt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsync-ssl

```bash
$ singularity exec <container> /usr/local/bin/rsync-ssl
$ podman run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runhmm.sh

```bash
$ singularity exec <container> /usr/local/bin/runhmm.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circos

```bash
$ singularity exec <container> /usr/local/bin/circos
$ podman run --it --rm --entrypoint /usr/local/bin/circos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circos.exe

```bash
$ singularity exec <container> /usr/local/bin/circos.exe
$ podman run --it --rm --entrypoint /usr/local/bin/circos.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circos.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile.bat

```bash
$ singularity exec <container> /usr/local/bin/compile.bat
$ podman run --it --rm --entrypoint /usr/local/bin/compile.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile.make

```bash
$ singularity exec <container> /usr/local/bin/compile.make
$ podman run --it --rm --entrypoint /usr/local/bin/compile.make   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile.make   -v ${PWD} -w ${PWD} <container> -c " $@"
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