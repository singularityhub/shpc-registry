---
layout: container
name:  "quay.io/biocontainers/fusion-filter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fusion-filter/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/fusion-filter/container.yaml"
updated_at: "2022-10-27 00:22:46.368882"
latest: "0.5.0--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/fusion-filter"
aliases:
 - ".fusion-filter-post-link.sh"
 - "blast_and_promiscuity_filter.pl"
 - "blast_check_pair.pl"
 - "blast_filter.pl"
 - "blast_outfmt6_replace_trans_id_w_gene_symbol.pl"
 - "build_chr_gene_alignment_index.pl"
 - "build_fusion_annot_db_index.pl"
 - "build_prot_info_db.pl"
 - "gencode_extract_relevant_gtf_exons.pl"
 - "gtf_file_to_feature_seqs.pl"
 - "gtf_to_exon_gene_records.pl"
 - "gtf_to_gene_spans.pl"
 - "index_blast_pairs.pl"
 - "index_blast_pairs.remove_gene_pair.pl"
 - "index_blast_pairs.remove_overlapping_genes.pl"
 - "index_cdna_seqs.pl"
 - "index_pfam_domain_info.pl"
 - "isoform_blast_gene_chr_conversion.pl"
 - "isoform_blast_mapping_indexer.pl"
 - "just_blast_test.pl"
 - "make_super_locus.pl"
 - "prep_genome_lib.pl"
 - "promiscuity_filter.pl"
 - "remove_long_intron_readthru_transcripts.pl"
versions:
 - "0.5.0--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for fusion-filter"
config: {"url": "https://biocontainers.pro/tools/fusion-filter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fusion-filter", "latest": {"0.5.0--hdfd78af_3": "sha256:6fc5fbea4f138208039a0a4f8383239dbfc68134ecc4570996869bff167e81f4"}, "tags": {"0.5.0--hdfd78af_3": "sha256:6fc5fbea4f138208039a0a4f8383239dbfc68134ecc4570996869bff167e81f4"}, "docker": "quay.io/biocontainers/fusion-filter", "aliases": {".fusion-filter-post-link.sh": "/usr/local/bin/.fusion-filter-post-link.sh", "blast_and_promiscuity_filter.pl": "/usr/local/bin/blast_and_promiscuity_filter.pl", "blast_check_pair.pl": "/usr/local/bin/blast_check_pair.pl", "blast_filter.pl": "/usr/local/bin/blast_filter.pl", "blast_outfmt6_replace_trans_id_w_gene_symbol.pl": "/usr/local/bin/blast_outfmt6_replace_trans_id_w_gene_symbol.pl", "build_chr_gene_alignment_index.pl": "/usr/local/bin/build_chr_gene_alignment_index.pl", "build_fusion_annot_db_index.pl": "/usr/local/bin/build_fusion_annot_db_index.pl", "build_prot_info_db.pl": "/usr/local/bin/build_prot_info_db.pl", "gencode_extract_relevant_gtf_exons.pl": "/usr/local/bin/gencode_extract_relevant_gtf_exons.pl", "gtf_file_to_feature_seqs.pl": "/usr/local/bin/gtf_file_to_feature_seqs.pl", "gtf_to_exon_gene_records.pl": "/usr/local/bin/gtf_to_exon_gene_records.pl", "gtf_to_gene_spans.pl": "/usr/local/bin/gtf_to_gene_spans.pl", "index_blast_pairs.pl": "/usr/local/bin/index_blast_pairs.pl", "index_blast_pairs.remove_gene_pair.pl": "/usr/local/bin/index_blast_pairs.remove_gene_pair.pl", "index_blast_pairs.remove_overlapping_genes.pl": "/usr/local/bin/index_blast_pairs.remove_overlapping_genes.pl", "index_cdna_seqs.pl": "/usr/local/bin/index_cdna_seqs.pl", "index_pfam_domain_info.pl": "/usr/local/bin/index_pfam_domain_info.pl", "isoform_blast_gene_chr_conversion.pl": "/usr/local/bin/isoform_blast_gene_chr_conversion.pl", "isoform_blast_mapping_indexer.pl": "/usr/local/bin/isoform_blast_mapping_indexer.pl", "just_blast_test.pl": "/usr/local/bin/just_blast_test.pl", "make_super_locus.pl": "/usr/local/bin/make_super_locus.pl", "prep_genome_lib.pl": "/usr/local/bin/prep_genome_lib.pl", "promiscuity_filter.pl": "/usr/local/bin/promiscuity_filter.pl", "remove_long_intron_readthru_transcripts.pl": "/usr/local/bin/remove_long_intron_readthru_transcripts.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fusion-filter.
shpc-registry automated BioContainers addition for fusion-filter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fusion-filter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fusion-filter:0.5.0--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fusion-filter/0.5.0--hdfd78af_3
$ module help quay.io/biocontainers/fusion-filter/0.5.0--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fusion-filter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fusion-filter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fusion-filter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fusion-filter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fusion-filter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fusion-filter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .fusion-filter-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.fusion-filter-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.fusion-filter-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.fusion-filter-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_and_promiscuity_filter.pl

```bash
$ singularity exec <container> /usr/local/bin/blast_and_promiscuity_filter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast_and_promiscuity_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_and_promiscuity_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_check_pair.pl

```bash
$ singularity exec <container> /usr/local/bin/blast_check_pair.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast_check_pair.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_check_pair.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_filter.pl

```bash
$ singularity exec <container> /usr/local/bin/blast_filter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_outfmt6_replace_trans_id_w_gene_symbol.pl

```bash
$ singularity exec <container> /usr/local/bin/blast_outfmt6_replace_trans_id_w_gene_symbol.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast_outfmt6_replace_trans_id_w_gene_symbol.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_outfmt6_replace_trans_id_w_gene_symbol.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_chr_gene_alignment_index.pl

```bash
$ singularity exec <container> /usr/local/bin/build_chr_gene_alignment_index.pl
$ podman run --it --rm --entrypoint /usr/local/bin/build_chr_gene_alignment_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_chr_gene_alignment_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_fusion_annot_db_index.pl

```bash
$ singularity exec <container> /usr/local/bin/build_fusion_annot_db_index.pl
$ podman run --it --rm --entrypoint /usr/local/bin/build_fusion_annot_db_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_fusion_annot_db_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_prot_info_db.pl

```bash
$ singularity exec <container> /usr/local/bin/build_prot_info_db.pl
$ podman run --it --rm --entrypoint /usr/local/bin/build_prot_info_db.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_prot_info_db.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gencode_extract_relevant_gtf_exons.pl

```bash
$ singularity exec <container> /usr/local/bin/gencode_extract_relevant_gtf_exons.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gencode_extract_relevant_gtf_exons.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gencode_extract_relevant_gtf_exons.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_file_to_feature_seqs.pl

```bash
$ singularity exec <container> /usr/local/bin/gtf_file_to_feature_seqs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_file_to_feature_seqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_file_to_feature_seqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_to_exon_gene_records.pl

```bash
$ singularity exec <container> /usr/local/bin/gtf_to_exon_gene_records.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_to_exon_gene_records.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_to_exon_gene_records.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_to_gene_spans.pl

```bash
$ singularity exec <container> /usr/local/bin/gtf_to_gene_spans.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_to_gene_spans.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_to_gene_spans.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_blast_pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/index_blast_pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/index_blast_pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_blast_pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_blast_pairs.remove_gene_pair.pl

```bash
$ singularity exec <container> /usr/local/bin/index_blast_pairs.remove_gene_pair.pl
$ podman run --it --rm --entrypoint /usr/local/bin/index_blast_pairs.remove_gene_pair.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_blast_pairs.remove_gene_pair.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_blast_pairs.remove_overlapping_genes.pl

```bash
$ singularity exec <container> /usr/local/bin/index_blast_pairs.remove_overlapping_genes.pl
$ podman run --it --rm --entrypoint /usr/local/bin/index_blast_pairs.remove_overlapping_genes.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_blast_pairs.remove_overlapping_genes.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_cdna_seqs.pl

```bash
$ singularity exec <container> /usr/local/bin/index_cdna_seqs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/index_cdna_seqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_cdna_seqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_pfam_domain_info.pl

```bash
$ singularity exec <container> /usr/local/bin/index_pfam_domain_info.pl
$ podman run --it --rm --entrypoint /usr/local/bin/index_pfam_domain_info.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_pfam_domain_info.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isoform_blast_gene_chr_conversion.pl

```bash
$ singularity exec <container> /usr/local/bin/isoform_blast_gene_chr_conversion.pl
$ podman run --it --rm --entrypoint /usr/local/bin/isoform_blast_gene_chr_conversion.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isoform_blast_gene_chr_conversion.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isoform_blast_mapping_indexer.pl

```bash
$ singularity exec <container> /usr/local/bin/isoform_blast_mapping_indexer.pl
$ podman run --it --rm --entrypoint /usr/local/bin/isoform_blast_mapping_indexer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isoform_blast_mapping_indexer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### just_blast_test.pl

```bash
$ singularity exec <container> /usr/local/bin/just_blast_test.pl
$ podman run --it --rm --entrypoint /usr/local/bin/just_blast_test.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/just_blast_test.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_super_locus.pl

```bash
$ singularity exec <container> /usr/local/bin/make_super_locus.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_super_locus.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_super_locus.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prep_genome_lib.pl

```bash
$ singularity exec <container> /usr/local/bin/prep_genome_lib.pl
$ podman run --it --rm --entrypoint /usr/local/bin/prep_genome_lib.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prep_genome_lib.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### promiscuity_filter.pl

```bash
$ singularity exec <container> /usr/local/bin/promiscuity_filter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/promiscuity_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/promiscuity_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_long_intron_readthru_transcripts.pl

```bash
$ singularity exec <container> /usr/local/bin/remove_long_intron_readthru_transcripts.pl
$ podman run --it --rm --entrypoint /usr/local/bin/remove_long_intron_readthru_transcripts.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_long_intron_readthru_transcripts.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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