package br.jus.tse.eleitoral.eleitor.integracao.webservices.rest;

import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import br.jus.tse.corporativa.arqjeespring.infra.exceptions.WebServicesException;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.dto.EleitorDTO;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.dto.EleitorSituacaoDTO;

@Path("/eleitores/")
@Produces({ MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
@Consumes({ MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
public interface IEleitorRESTService {

	@GET
	@Path("/{pId}")
	@Produces({ MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
	public EleitorDTO pesquisarPeloId(@PathParam("pId") String pId) throws WebServicesException;
	
	// restante dos serviços para CRUD
	/*@POST
	@Produces({ MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
	@Consumes({ MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
	EleitorDTO adicionar(EleitorDTO pItemDTO) throws ServiceException;

	@PUT
	@Produces({ MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
	@Consumes({ MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
	EleitorDTO alterar(EleitorDTO pItemDTO) throws ServiceException;

	@DELETE
	@Path("/{pId}")
	@Produces({ MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
	@Consumes({ MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
	Response remover(@PathParam("pId") Integer pId) throws ServiceException;

	@GET
	@Produces({ MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
	List<EleitorDTO> pesquisarTodos() throws ServiceException;*/

	@GET
	@Path("/{pId}")
	@Produces({ MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
	public EleitorSituacaoDTO pesquisarSituacao(@PathParam("pId") String pId) throws WebServicesException;

}
