import Repository from './Repository';

const resource = '/photos'

export default {
    get(pageId) {
        return Repository.get(`${resource}/?page=${pageId}`);
    },

    get_next_page(currentPage){
        return Repository.get(`${resource}/?page=${currentPage+1}`)
    },

    get_last_page(totalPages) {
        return Repository.get(`${resource}/?page=${totalPages}`)
    },

    get_previous_page(currentPage) {
        return Repository.get(`${resource}/?page=${currentPage-1}`)
    },

    get_first_page() {
        return Repository.get(`${resource}/`)
    },

    getPhoto(photoID){
        return Repository.get(`${resource}/${photoID}/detail/`);
    },

    createPhoto(payload){
        return Repository.post(`${resource}/create/`, payload);
    },

    updatePhoto(photoID, payload){
        return Repository.patch(`${resource}/${photoID}/update/`, payload)
    },

    deletePhoto(photoID){
        return Repository.post(`${resource}/${photoID}/delete/`);
    }
}