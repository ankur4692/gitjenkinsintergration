provider "github" {
  token = "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"
}

resource "github_repository" "terraform-first-repo" {
  name        = "My_Firest_repo_terrafrom12"
  description = "My_Firest_repo_through_terrafrom_"
  visibility = "public"
  auto_init = true
}
