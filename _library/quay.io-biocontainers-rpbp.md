---
layout: container
name:  "quay.io/biocontainers/rpbp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rpbp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rpbp/container.yaml"
updated_at: "2025-11-26 03:27:26.093745"
latest: "3.0.4--py310h184ae93_3"
container_url: "https://biocontainers.pro/tools/rpbp"
aliases:
 - "add-mygene-info-to-orfs"
 - "bam-to-wiggle"
 - "bed12-to-gtf"
 - "bedx-to-bedy"
 - "cmdstan_model"
 - "collect-read-length-orf-profiles"
 - "compile-rpbp-models"
 - "convert-ccds-to-bed"
 - "count-aligned-reads"
 - "count-reads"
 - "create-base-genome-profile"
 - "create-mygene-report"
 - "create-orf-profiles"
 - "create-read-length-orf-profiles"
 - "dash-generate-components"
 - "dash-update-components"
 - "dask"
 - "dna-to-aa"
 - "download-srr-files"
 - "epylint"
 - "estimate-metagene-profile-bayes-factors"
 - "estimate-orf-bayes-factors"
 - "extract-bed-sequences"
 - "extract-cds-coordinates"
 - "extract-metagene-profiles"
 - "extract-orf-coordinates"
 - "extract-orf-profiles"
 - "fasta-to-fastq"
 - "fastq-pe-dedupe"
 - "filter-bam-by-ids"
 - "filter-nonunique-peptide-matches"
 - "fix-all-bed-files"
 - "flexbar"
 - "geo2fastq"
 - "get-all-orf-peptide-matches"
 - "get-all-read-filtering-counts"
 - "get-all-utrs"
 - "get-orf-peptide-matches"
 - "get-read-length-distribution"
 - "gtf-to-bed12"
 - "install_cmdstan"
 - "install_cxx_toolchain"
 - "isort"
 - "isort-identify-imports"
 - "join-long-chromosomes"
 - "label-orfs"
 - "merge-isoforms"
 - "merge-replicate-orf-profiles"
 - "parmed"
 - "predict-translated-orfs"
 - "prepare-rpbp-genome"
 - "pyensembl"
 - "pylint"
 - "pylint-config"
 - "pyreverse"
 - "remove-duplicate-bed-entries"
 - "remove-duplicate-sequences"
 - "remove-multimapping-reads"
 - "renderer"
 - "reorder-fasta"
 - "rpbp-predictions-dashboard"
 - "rpbp-profile-construction-dashboard"
 - "run-all-rpbp-instances"
 - "run-bowtie"
 - "run-rpbp-pipeline"
 - "run-signalp"
 - "run-tmhmm"
 - "select-final-prediction-set"
 - "select-periodic-offsets"
 - "split-bed12-blocks"
 - "split-long-chromosomes"
 - "subtract-bed"
 - "summarize-rpbp-predictions"
 - "summarize-rpbp-profile-construction"
 - "symilar"
 - "visualize-metagene-profile-bayes-factor"
 - "visualize-orf-type-metagene-profiles"
 - "STAR"
 - "STARlong"
 - "hwloc-gather-cpuid"
 - "hwloc-annotate"
 - "hwloc-bind"
 - "hwloc-calc"
 - "hwloc-compress-dir"
 - "hwloc-diff"
 - "hwloc-distrib"
 - "hwloc-gather-topology"
 - "hwloc-info"
 - "hwloc-ls"
 - "hwloc-patch"
 - "hwloc-ps"
 - "lstopo"
 - "lstopo-no-graphics"
 - "dask-scheduler"
 - "dask-ssh"
 - "dask-worker"
 - "fastqc"
 - "flask"
 - "get_objgraph"
 - "undill"
 - "bokeh"
 - "jpackage"
versions:
 - "3.0.1--py38h4a32c8e_0"
 - "3.0.2--py310h0dbaff4_1"
 - "3.0.2--py39h1f90b4d_1"
 - "3.0.4--py310h0dbaff4_0"
 - "3.0.4--py39h9e0f934_1"
 - "3.0.4--py310h184ae93_2"
 - "3.0.4--py310h184ae93_3"
description: "singularity registry hpc automated addition for rpbp"
config: {"url": "https://biocontainers.pro/tools/rpbp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rpbp", "latest": {"3.0.4--py310h184ae93_3": "sha256:5552ff74f67d97946deca4371f79325cac16735b00b2a41f428b00a4a6099887"}, "tags": {"3.0.1--py38h4a32c8e_0": "sha256:2be22cc25f5969f212e96e948fdd176061d714796377b1fd4141bbe04d244f60", "3.0.2--py310h0dbaff4_1": "sha256:0d7cdfeb2ffeb093b1c94cc169594467695ed278270a290e4e1b4dfb6536d6f9", "3.0.2--py39h1f90b4d_1": "sha256:ff54eda9bf074c64ea5a30576b108624de8a3a4f65b86c2e1f4434f372d0f50f", "3.0.4--py310h0dbaff4_0": "sha256:2e78526cde7234b6427f2f299666d4ddfcfbcfde8ad0ae24ba648c4ba7134b63", "3.0.4--py39h9e0f934_1": "sha256:7136e838365c6181e7165e480d411748d988f84986455be9315c6906b70122c3", "3.0.4--py310h184ae93_2": "sha256:0c3c1f2333f801f9aca6281c66d1df8e9998a5d53271c4fcb5bd48b528da4c18", "3.0.4--py310h184ae93_3": "sha256:5552ff74f67d97946deca4371f79325cac16735b00b2a41f428b00a4a6099887"}, "docker": "quay.io/biocontainers/rpbp", "aliases": {"add-mygene-info-to-orfs": "/usr/local/bin/add-mygene-info-to-orfs", "bam-to-wiggle": "/usr/local/bin/bam-to-wiggle", "bed12-to-gtf": "/usr/local/bin/bed12-to-gtf", "bedx-to-bedy": "/usr/local/bin/bedx-to-bedy", "cmdstan_model": "/usr/local/bin/cmdstan_model", "collect-read-length-orf-profiles": "/usr/local/bin/collect-read-length-orf-profiles", "compile-rpbp-models": "/usr/local/bin/compile-rpbp-models", "convert-ccds-to-bed": "/usr/local/bin/convert-ccds-to-bed", "count-aligned-reads": "/usr/local/bin/count-aligned-reads", "count-reads": "/usr/local/bin/count-reads", "create-base-genome-profile": "/usr/local/bin/create-base-genome-profile", "create-mygene-report": "/usr/local/bin/create-mygene-report", "create-orf-profiles": "/usr/local/bin/create-orf-profiles", "create-read-length-orf-profiles": "/usr/local/bin/create-read-length-orf-profiles", "dash-generate-components": "/usr/local/bin/dash-generate-components", "dash-update-components": "/usr/local/bin/dash-update-components", "dask": "/usr/local/bin/dask", "dna-to-aa": "/usr/local/bin/dna-to-aa", "download-srr-files": "/usr/local/bin/download-srr-files", "epylint": "/usr/local/bin/epylint", "estimate-metagene-profile-bayes-factors": "/usr/local/bin/estimate-metagene-profile-bayes-factors", "estimate-orf-bayes-factors": "/usr/local/bin/estimate-orf-bayes-factors", "extract-bed-sequences": "/usr/local/bin/extract-bed-sequences", "extract-cds-coordinates": "/usr/local/bin/extract-cds-coordinates", "extract-metagene-profiles": "/usr/local/bin/extract-metagene-profiles", "extract-orf-coordinates": "/usr/local/bin/extract-orf-coordinates", "extract-orf-profiles": "/usr/local/bin/extract-orf-profiles", "fasta-to-fastq": "/usr/local/bin/fasta-to-fastq", "fastq-pe-dedupe": "/usr/local/bin/fastq-pe-dedupe", "filter-bam-by-ids": "/usr/local/bin/filter-bam-by-ids", "filter-nonunique-peptide-matches": "/usr/local/bin/filter-nonunique-peptide-matches", "fix-all-bed-files": "/usr/local/bin/fix-all-bed-files", "flexbar": "/usr/local/bin/flexbar", "geo2fastq": "/usr/local/bin/geo2fastq", "get-all-orf-peptide-matches": "/usr/local/bin/get-all-orf-peptide-matches", "get-all-read-filtering-counts": "/usr/local/bin/get-all-read-filtering-counts", "get-all-utrs": "/usr/local/bin/get-all-utrs", "get-orf-peptide-matches": "/usr/local/bin/get-orf-peptide-matches", "get-read-length-distribution": "/usr/local/bin/get-read-length-distribution", "gtf-to-bed12": "/usr/local/bin/gtf-to-bed12", "install_cmdstan": "/usr/local/bin/install_cmdstan", "install_cxx_toolchain": "/usr/local/bin/install_cxx_toolchain", "isort": "/usr/local/bin/isort", "isort-identify-imports": "/usr/local/bin/isort-identify-imports", "join-long-chromosomes": "/usr/local/bin/join-long-chromosomes", "label-orfs": "/usr/local/bin/label-orfs", "merge-isoforms": "/usr/local/bin/merge-isoforms", "merge-replicate-orf-profiles": "/usr/local/bin/merge-replicate-orf-profiles", "parmed": "/usr/local/bin/parmed", "predict-translated-orfs": "/usr/local/bin/predict-translated-orfs", "prepare-rpbp-genome": "/usr/local/bin/prepare-rpbp-genome", "pyensembl": "/usr/local/bin/pyensembl", "pylint": "/usr/local/bin/pylint", "pylint-config": "/usr/local/bin/pylint-config", "pyreverse": "/usr/local/bin/pyreverse", "remove-duplicate-bed-entries": "/usr/local/bin/remove-duplicate-bed-entries", "remove-duplicate-sequences": "/usr/local/bin/remove-duplicate-sequences", "remove-multimapping-reads": "/usr/local/bin/remove-multimapping-reads", "renderer": "/usr/local/bin/renderer", "reorder-fasta": "/usr/local/bin/reorder-fasta", "rpbp-predictions-dashboard": "/usr/local/bin/rpbp-predictions-dashboard", "rpbp-profile-construction-dashboard": "/usr/local/bin/rpbp-profile-construction-dashboard", "run-all-rpbp-instances": "/usr/local/bin/run-all-rpbp-instances", "run-bowtie": "/usr/local/bin/run-bowtie", "run-rpbp-pipeline": "/usr/local/bin/run-rpbp-pipeline", "run-signalp": "/usr/local/bin/run-signalp", "run-tmhmm": "/usr/local/bin/run-tmhmm", "select-final-prediction-set": "/usr/local/bin/select-final-prediction-set", "select-periodic-offsets": "/usr/local/bin/select-periodic-offsets", "split-bed12-blocks": "/usr/local/bin/split-bed12-blocks", "split-long-chromosomes": "/usr/local/bin/split-long-chromosomes", "subtract-bed": "/usr/local/bin/subtract-bed", "summarize-rpbp-predictions": "/usr/local/bin/summarize-rpbp-predictions", "summarize-rpbp-profile-construction": "/usr/local/bin/summarize-rpbp-profile-construction", "symilar": "/usr/local/bin/symilar", "visualize-metagene-profile-bayes-factor": "/usr/local/bin/visualize-metagene-profile-bayes-factor", "visualize-orf-type-metagene-profiles": "/usr/local/bin/visualize-orf-type-metagene-profiles", "STAR": "/usr/local/bin/STAR", "STARlong": "/usr/local/bin/STARlong", "hwloc-gather-cpuid": "/usr/local/bin/hwloc-gather-cpuid", "hwloc-annotate": "/usr/local/bin/hwloc-annotate", "hwloc-bind": "/usr/local/bin/hwloc-bind", "hwloc-calc": "/usr/local/bin/hwloc-calc", "hwloc-compress-dir": "/usr/local/bin/hwloc-compress-dir", "hwloc-diff": "/usr/local/bin/hwloc-diff", "hwloc-distrib": "/usr/local/bin/hwloc-distrib", "hwloc-gather-topology": "/usr/local/bin/hwloc-gather-topology", "hwloc-info": "/usr/local/bin/hwloc-info", "hwloc-ls": "/usr/local/bin/hwloc-ls", "hwloc-patch": "/usr/local/bin/hwloc-patch", "hwloc-ps": "/usr/local/bin/hwloc-ps", "lstopo": "/usr/local/bin/lstopo", "lstopo-no-graphics": "/usr/local/bin/lstopo-no-graphics", "dask-scheduler": "/usr/local/bin/dask-scheduler", "dask-ssh": "/usr/local/bin/dask-ssh", "dask-worker": "/usr/local/bin/dask-worker", "fastqc": "/usr/local/bin/fastqc", "flask": "/usr/local/bin/flask", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "bokeh": "/usr/local/bin/bokeh", "jpackage": "/usr/local/bin/jpackage"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rpbp.
singularity registry hpc automated addition for rpbp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rpbp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rpbp:3.0.4--py310h184ae93_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rpbp/3.0.4--py310h184ae93_3
$ module help quay.io/biocontainers/rpbp/3.0.4--py310h184ae93_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rpbp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rpbp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rpbp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rpbp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rpbp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rpbp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add-mygene-info-to-orfs

```bash
$ singularity exec <container> /usr/local/bin/add-mygene-info-to-orfs
$ podman run --it --rm --entrypoint /usr/local/bin/add-mygene-info-to-orfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add-mygene-info-to-orfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam-to-wiggle

```bash
$ singularity exec <container> /usr/local/bin/bam-to-wiggle
$ podman run --it --rm --entrypoint /usr/local/bin/bam-to-wiggle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam-to-wiggle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed12-to-gtf

```bash
$ singularity exec <container> /usr/local/bin/bed12-to-gtf
$ podman run --it --rm --entrypoint /usr/local/bin/bed12-to-gtf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed12-to-gtf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedx-to-bedy

```bash
$ singularity exec <container> /usr/local/bin/bedx-to-bedy
$ podman run --it --rm --entrypoint /usr/local/bin/bedx-to-bedy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedx-to-bedy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmdstan_model

```bash
$ singularity exec <container> /usr/local/bin/cmdstan_model
$ podman run --it --rm --entrypoint /usr/local/bin/cmdstan_model   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmdstan_model   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### collect-read-length-orf-profiles

```bash
$ singularity exec <container> /usr/local/bin/collect-read-length-orf-profiles
$ podman run --it --rm --entrypoint /usr/local/bin/collect-read-length-orf-profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/collect-read-length-orf-profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile-rpbp-models

```bash
$ singularity exec <container> /usr/local/bin/compile-rpbp-models
$ podman run --it --rm --entrypoint /usr/local/bin/compile-rpbp-models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile-rpbp-models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-ccds-to-bed

```bash
$ singularity exec <container> /usr/local/bin/convert-ccds-to-bed
$ podman run --it --rm --entrypoint /usr/local/bin/convert-ccds-to-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-ccds-to-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### count-aligned-reads

```bash
$ singularity exec <container> /usr/local/bin/count-aligned-reads
$ podman run --it --rm --entrypoint /usr/local/bin/count-aligned-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count-aligned-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### count-reads

```bash
$ singularity exec <container> /usr/local/bin/count-reads
$ podman run --it --rm --entrypoint /usr/local/bin/count-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create-base-genome-profile

```bash
$ singularity exec <container> /usr/local/bin/create-base-genome-profile
$ podman run --it --rm --entrypoint /usr/local/bin/create-base-genome-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create-base-genome-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create-mygene-report

```bash
$ singularity exec <container> /usr/local/bin/create-mygene-report
$ podman run --it --rm --entrypoint /usr/local/bin/create-mygene-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create-mygene-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create-orf-profiles

```bash
$ singularity exec <container> /usr/local/bin/create-orf-profiles
$ podman run --it --rm --entrypoint /usr/local/bin/create-orf-profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create-orf-profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create-read-length-orf-profiles

```bash
$ singularity exec <container> /usr/local/bin/create-read-length-orf-profiles
$ podman run --it --rm --entrypoint /usr/local/bin/create-read-length-orf-profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create-read-length-orf-profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dash-generate-components

```bash
$ singularity exec <container> /usr/local/bin/dash-generate-components
$ podman run --it --rm --entrypoint /usr/local/bin/dash-generate-components   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dash-generate-components   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dash-update-components

```bash
$ singularity exec <container> /usr/local/bin/dash-update-components
$ podman run --it --rm --entrypoint /usr/local/bin/dash-update-components   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dash-update-components   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask

```bash
$ singularity exec <container> /usr/local/bin/dask
$ podman run --it --rm --entrypoint /usr/local/bin/dask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dna-to-aa

```bash
$ singularity exec <container> /usr/local/bin/dna-to-aa
$ podman run --it --rm --entrypoint /usr/local/bin/dna-to-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dna-to-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-srr-files

```bash
$ singularity exec <container> /usr/local/bin/download-srr-files
$ podman run --it --rm --entrypoint /usr/local/bin/download-srr-files   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-srr-files   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### epylint

```bash
$ singularity exec <container> /usr/local/bin/epylint
$ podman run --it --rm --entrypoint /usr/local/bin/epylint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epylint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estimate-metagene-profile-bayes-factors

```bash
$ singularity exec <container> /usr/local/bin/estimate-metagene-profile-bayes-factors
$ podman run --it --rm --entrypoint /usr/local/bin/estimate-metagene-profile-bayes-factors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estimate-metagene-profile-bayes-factors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estimate-orf-bayes-factors

```bash
$ singularity exec <container> /usr/local/bin/estimate-orf-bayes-factors
$ podman run --it --rm --entrypoint /usr/local/bin/estimate-orf-bayes-factors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estimate-orf-bayes-factors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract-bed-sequences

```bash
$ singularity exec <container> /usr/local/bin/extract-bed-sequences
$ podman run --it --rm --entrypoint /usr/local/bin/extract-bed-sequences   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract-bed-sequences   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract-cds-coordinates

```bash
$ singularity exec <container> /usr/local/bin/extract-cds-coordinates
$ podman run --it --rm --entrypoint /usr/local/bin/extract-cds-coordinates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract-cds-coordinates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract-metagene-profiles

```bash
$ singularity exec <container> /usr/local/bin/extract-metagene-profiles
$ podman run --it --rm --entrypoint /usr/local/bin/extract-metagene-profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract-metagene-profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract-orf-coordinates

```bash
$ singularity exec <container> /usr/local/bin/extract-orf-coordinates
$ podman run --it --rm --entrypoint /usr/local/bin/extract-orf-coordinates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract-orf-coordinates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract-orf-profiles

```bash
$ singularity exec <container> /usr/local/bin/extract-orf-profiles
$ podman run --it --rm --entrypoint /usr/local/bin/extract-orf-profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract-orf-profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-to-fastq

```bash
$ singularity exec <container> /usr/local/bin/fasta-to-fastq
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-to-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-to-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-pe-dedupe

```bash
$ singularity exec <container> /usr/local/bin/fastq-pe-dedupe
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-pe-dedupe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-pe-dedupe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-bam-by-ids

```bash
$ singularity exec <container> /usr/local/bin/filter-bam-by-ids
$ podman run --it --rm --entrypoint /usr/local/bin/filter-bam-by-ids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-bam-by-ids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-nonunique-peptide-matches

```bash
$ singularity exec <container> /usr/local/bin/filter-nonunique-peptide-matches
$ podman run --it --rm --entrypoint /usr/local/bin/filter-nonunique-peptide-matches   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-nonunique-peptide-matches   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix-all-bed-files

```bash
$ singularity exec <container> /usr/local/bin/fix-all-bed-files
$ podman run --it --rm --entrypoint /usr/local/bin/fix-all-bed-files   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix-all-bed-files   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flexbar

```bash
$ singularity exec <container> /usr/local/bin/flexbar
$ podman run --it --rm --entrypoint /usr/local/bin/flexbar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flexbar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geo2fastq

```bash
$ singularity exec <container> /usr/local/bin/geo2fastq
$ podman run --it --rm --entrypoint /usr/local/bin/geo2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geo2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get-all-orf-peptide-matches

```bash
$ singularity exec <container> /usr/local/bin/get-all-orf-peptide-matches
$ podman run --it --rm --entrypoint /usr/local/bin/get-all-orf-peptide-matches   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get-all-orf-peptide-matches   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get-all-read-filtering-counts

```bash
$ singularity exec <container> /usr/local/bin/get-all-read-filtering-counts
$ podman run --it --rm --entrypoint /usr/local/bin/get-all-read-filtering-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get-all-read-filtering-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get-all-utrs

```bash
$ singularity exec <container> /usr/local/bin/get-all-utrs
$ podman run --it --rm --entrypoint /usr/local/bin/get-all-utrs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get-all-utrs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get-orf-peptide-matches

```bash
$ singularity exec <container> /usr/local/bin/get-orf-peptide-matches
$ podman run --it --rm --entrypoint /usr/local/bin/get-orf-peptide-matches   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get-orf-peptide-matches   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get-read-length-distribution

```bash
$ singularity exec <container> /usr/local/bin/get-read-length-distribution
$ podman run --it --rm --entrypoint /usr/local/bin/get-read-length-distribution   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get-read-length-distribution   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf-to-bed12

```bash
$ singularity exec <container> /usr/local/bin/gtf-to-bed12
$ podman run --it --rm --entrypoint /usr/local/bin/gtf-to-bed12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf-to-bed12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### install_cmdstan

```bash
$ singularity exec <container> /usr/local/bin/install_cmdstan
$ podman run --it --rm --entrypoint /usr/local/bin/install_cmdstan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/install_cmdstan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### install_cxx_toolchain

```bash
$ singularity exec <container> /usr/local/bin/install_cxx_toolchain
$ podman run --it --rm --entrypoint /usr/local/bin/install_cxx_toolchain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/install_cxx_toolchain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isort

```bash
$ singularity exec <container> /usr/local/bin/isort
$ podman run --it --rm --entrypoint /usr/local/bin/isort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isort-identify-imports

```bash
$ singularity exec <container> /usr/local/bin/isort-identify-imports
$ podman run --it --rm --entrypoint /usr/local/bin/isort-identify-imports   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isort-identify-imports   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### join-long-chromosomes

```bash
$ singularity exec <container> /usr/local/bin/join-long-chromosomes
$ podman run --it --rm --entrypoint /usr/local/bin/join-long-chromosomes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/join-long-chromosomes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### label-orfs

```bash
$ singularity exec <container> /usr/local/bin/label-orfs
$ podman run --it --rm --entrypoint /usr/local/bin/label-orfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/label-orfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-isoforms

```bash
$ singularity exec <container> /usr/local/bin/merge-isoforms
$ podman run --it --rm --entrypoint /usr/local/bin/merge-isoforms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-isoforms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-replicate-orf-profiles

```bash
$ singularity exec <container> /usr/local/bin/merge-replicate-orf-profiles
$ podman run --it --rm --entrypoint /usr/local/bin/merge-replicate-orf-profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-replicate-orf-profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parmed

```bash
$ singularity exec <container> /usr/local/bin/parmed
$ podman run --it --rm --entrypoint /usr/local/bin/parmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### predict-translated-orfs

```bash
$ singularity exec <container> /usr/local/bin/predict-translated-orfs
$ podman run --it --rm --entrypoint /usr/local/bin/predict-translated-orfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/predict-translated-orfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepare-rpbp-genome

```bash
$ singularity exec <container> /usr/local/bin/prepare-rpbp-genome
$ podman run --it --rm --entrypoint /usr/local/bin/prepare-rpbp-genome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepare-rpbp-genome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyensembl

```bash
$ singularity exec <container> /usr/local/bin/pyensembl
$ podman run --it --rm --entrypoint /usr/local/bin/pyensembl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyensembl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pylint

```bash
$ singularity exec <container> /usr/local/bin/pylint
$ podman run --it --rm --entrypoint /usr/local/bin/pylint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pylint-config

```bash
$ singularity exec <container> /usr/local/bin/pylint-config
$ podman run --it --rm --entrypoint /usr/local/bin/pylint-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylint-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyreverse

```bash
$ singularity exec <container> /usr/local/bin/pyreverse
$ podman run --it --rm --entrypoint /usr/local/bin/pyreverse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyreverse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove-duplicate-bed-entries

```bash
$ singularity exec <container> /usr/local/bin/remove-duplicate-bed-entries
$ podman run --it --rm --entrypoint /usr/local/bin/remove-duplicate-bed-entries   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove-duplicate-bed-entries   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove-duplicate-sequences

```bash
$ singularity exec <container> /usr/local/bin/remove-duplicate-sequences
$ podman run --it --rm --entrypoint /usr/local/bin/remove-duplicate-sequences   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove-duplicate-sequences   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove-multimapping-reads

```bash
$ singularity exec <container> /usr/local/bin/remove-multimapping-reads
$ podman run --it --rm --entrypoint /usr/local/bin/remove-multimapping-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove-multimapping-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### renderer

```bash
$ singularity exec <container> /usr/local/bin/renderer
$ podman run --it --rm --entrypoint /usr/local/bin/renderer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/renderer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reorder-fasta

```bash
$ singularity exec <container> /usr/local/bin/reorder-fasta
$ podman run --it --rm --entrypoint /usr/local/bin/reorder-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reorder-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rpbp-predictions-dashboard

```bash
$ singularity exec <container> /usr/local/bin/rpbp-predictions-dashboard
$ podman run --it --rm --entrypoint /usr/local/bin/rpbp-predictions-dashboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rpbp-predictions-dashboard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rpbp-profile-construction-dashboard

```bash
$ singularity exec <container> /usr/local/bin/rpbp-profile-construction-dashboard
$ podman run --it --rm --entrypoint /usr/local/bin/rpbp-profile-construction-dashboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rpbp-profile-construction-dashboard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-all-rpbp-instances

```bash
$ singularity exec <container> /usr/local/bin/run-all-rpbp-instances
$ podman run --it --rm --entrypoint /usr/local/bin/run-all-rpbp-instances   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-all-rpbp-instances   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-bowtie

```bash
$ singularity exec <container> /usr/local/bin/run-bowtie
$ podman run --it --rm --entrypoint /usr/local/bin/run-bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-rpbp-pipeline

```bash
$ singularity exec <container> /usr/local/bin/run-rpbp-pipeline
$ podman run --it --rm --entrypoint /usr/local/bin/run-rpbp-pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-rpbp-pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-signalp

```bash
$ singularity exec <container> /usr/local/bin/run-signalp
$ podman run --it --rm --entrypoint /usr/local/bin/run-signalp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-signalp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-tmhmm

```bash
$ singularity exec <container> /usr/local/bin/run-tmhmm
$ podman run --it --rm --entrypoint /usr/local/bin/run-tmhmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-tmhmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select-final-prediction-set

```bash
$ singularity exec <container> /usr/local/bin/select-final-prediction-set
$ podman run --it --rm --entrypoint /usr/local/bin/select-final-prediction-set   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select-final-prediction-set   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select-periodic-offsets

```bash
$ singularity exec <container> /usr/local/bin/select-periodic-offsets
$ podman run --it --rm --entrypoint /usr/local/bin/select-periodic-offsets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select-periodic-offsets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split-bed12-blocks

```bash
$ singularity exec <container> /usr/local/bin/split-bed12-blocks
$ podman run --it --rm --entrypoint /usr/local/bin/split-bed12-blocks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split-bed12-blocks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split-long-chromosomes

```bash
$ singularity exec <container> /usr/local/bin/split-long-chromosomes
$ podman run --it --rm --entrypoint /usr/local/bin/split-long-chromosomes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split-long-chromosomes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subtract-bed

```bash
$ singularity exec <container> /usr/local/bin/subtract-bed
$ podman run --it --rm --entrypoint /usr/local/bin/subtract-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subtract-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summarize-rpbp-predictions

```bash
$ singularity exec <container> /usr/local/bin/summarize-rpbp-predictions
$ podman run --it --rm --entrypoint /usr/local/bin/summarize-rpbp-predictions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarize-rpbp-predictions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summarize-rpbp-profile-construction

```bash
$ singularity exec <container> /usr/local/bin/summarize-rpbp-profile-construction
$ podman run --it --rm --entrypoint /usr/local/bin/summarize-rpbp-profile-construction   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarize-rpbp-profile-construction   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### symilar

```bash
$ singularity exec <container> /usr/local/bin/symilar
$ podman run --it --rm --entrypoint /usr/local/bin/symilar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/symilar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### visualize-metagene-profile-bayes-factor

```bash
$ singularity exec <container> /usr/local/bin/visualize-metagene-profile-bayes-factor
$ podman run --it --rm --entrypoint /usr/local/bin/visualize-metagene-profile-bayes-factor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/visualize-metagene-profile-bayes-factor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### visualize-orf-type-metagene-profiles

```bash
$ singularity exec <container> /usr/local/bin/visualize-orf-type-metagene-profiles
$ podman run --it --rm --entrypoint /usr/local/bin/visualize-orf-type-metagene-profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/visualize-orf-type-metagene-profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR

```bash
$ singularity exec <container> /usr/local/bin/STAR
$ podman run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong

```bash
$ singularity exec <container> /usr/local/bin/STARlong
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### dask-scheduler

```bash
$ singularity exec <container> /usr/local/bin/dask-scheduler
$ podman run --it --rm --entrypoint /usr/local/bin/dask-scheduler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-scheduler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-ssh

```bash
$ singularity exec <container> /usr/local/bin/dask-ssh
$ podman run --it --rm --entrypoint /usr/local/bin/dask-ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-worker

```bash
$ singularity exec <container> /usr/local/bin/dask-worker
$ podman run --it --rm --entrypoint /usr/local/bin/dask-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqc

```bash
$ singularity exec <container> /usr/local/bin/fastqc
$ podman run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bokeh

```bash
$ singularity exec <container> /usr/local/bin/bokeh
$ podman run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
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