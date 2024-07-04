import requests

# Reemplaza con tu token de acceso obtenido
ACCESS_TOKEN = 'TU_ACCESS_TOKEN'
USER_ID = 'me'  # Puedes usar 'me' para obtener datos del usuario autenticado
BASE_URL = 'https://graph.instagram.com'

def get_user_media(user_id, access_token):
    url = f'{BASE_URL}/{user_id}/media'
    params = {
        'fields': 'id,caption,media_type,media_url,thumbnail_url,permalink,timestamp,username,like_count,comments_count',
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []

def main():
    media = get_user_media(USER_ID, ACCESS_TOKEN)
    
    if not media:
        print("No se encontraron publicaciones.")
        return

    # Ordenar por likes y comentarios
    media_sorted_by_likes = sorted(media, key=lambda x: x.get('like_count', 0), reverse=True)
    media_sorted_by_comments = sorted(media, key=lambda x: x.get('comments_count', 0), reverse=True)
    
    print("Publicaciones con más likes:")
    for post in media_sorted_by_likes[:5]:  # Mostrar las top 5 publicaciones
        print(f"URL: {post['permalink']}, Likes: {post.get('like_count', 0)}, Comentarios: {post.get('comments_count', 0)}")

    print("\nPublicaciones con más comentarios:")
    for post in media_sorted_by_comments[:5]:  # Mostrar las top 5 publicaciones
        print(f"URL: {post['permalink']}, Likes: {post.get('like_count', 0)}, Comentarios: {post.get('comments_count', 0)}")

if __name__ == "__main__":
    main()
