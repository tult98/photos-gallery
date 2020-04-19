import PhotosRepository from "./photosRepository"

const repositories = {
    photos: PhotosRepository,
}

export const RepositoryFactory = {
    get: name => repositories[name]
};